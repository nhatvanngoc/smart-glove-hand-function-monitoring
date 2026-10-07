# -*- coding: utf-8 -*-
"""
freecad_compat.py — Lớp tương thích TỐI THIỂU của API FreeCAD (App / Part / Mesh)
trên OCCT (gói OCP), để CÙNG một script build_*.py có thể:

  1) chạy nguyên văn trên FreeCAD thật (GUI hoặc `freecadcmd build_xxx.py`)
  2) chạy headless trong CI/container không cài FreeCAD để KIỂM TRA HÌNH HỌC:
     hợp lệ solid, kín, thể tích, bao hình (kiểm tra ràng buộc ΔX ≤ 2 mm...), xuất STL.

Đây KHÔNG phải FreeCAD. Nó chỉ mô phỏng đúng tập API mà các script trong thư mục này
dùng: Polygon → Face → extrude/prism, boolean Cut/Fuse/Common, biến đổi, khối cơ bản,
thuộc tính Volume/BoundBox, Mesh.export. Cùng một kernel hình học (OCCT) nên kết quả
hình học trùng khớp với FreeCAD.
"""
import math
import os

from OCP.gp import gp_Pnt, gp_Vec, gp_Dir, gp_Ax1, gp_Ax2, gp_Trsf
from OCP.TopoDS import TopoDS
from OCP.BRepBuilderAPI import (BRepBuilderAPI_MakePolygon, BRepBuilderAPI_MakeFace,
                                BRepBuilderAPI_Transform, BRepBuilderAPI_MakeEdge)
from OCP.BRepPrimAPI import (BRepPrimAPI_MakePrism, BRepPrimAPI_MakeBox,
                             BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeCone)
from OCP.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse, BRepAlgoAPI_Common, BRepAlgoAPI_BuilderAlgo
from OCP.ShapeUpgrade import ShapeUpgrade_UnifySameDomain
from OCP.TopTools import TopTools_ListOfShape
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_SOLID, TopAbs_FACE, TopAbs_WIRE
from OCP.BRepGProp import BRepGProp
from OCP.GProp import GProp_GProps
from OCP.Bnd import Bnd_Box
from OCP.BRepBndLib import BRepBndLib
from OCP.BRepCheck import BRepCheck_Analyzer
from OCP.BRepMesh import BRepMesh_IncrementalMesh
from OCP.StlAPI import StlAPI_Writer
from OCP.BRep import BRep_Tool
from OCP.TopLoc import TopLoc_Location


# =============================================================================
# Vector
# =============================================================================
class Vector(object):
    __slots__ = ("x", "y", "z")

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x, self.y, self.z = float(x), float(y), float(z)

    # --- phép toán ---
    def __add__(self, o):
        return Vector(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o):
        return Vector(self.x - o.x, self.y - o.y, self.z - o.z)

    def __mul__(self, s):
        return Vector(self.x * s, self.y * s, self.z * s)

    __rmul__ = __mul__

    def __truediv__(self, s):
        return Vector(self.x / s, self.y / s, self.z / s)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def __repr__(self):
        return "Vector (%.4f, %.4f, %.4f)" % (self.x, self.y, self.z)

    @property
    def Length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        L = self.Length or 1.0
        self.x, self.y, self.z = self.x / L, self.y / L, self.z / L

    def normalized(self):
        L = self.Length or 1.0
        return Vector(self.x / L, self.y / L, self.z / L)

    def cross(self, o):
        return Vector(self.y * o.z - self.z * o.y,
                      self.z * o.x - self.x * o.z,
                      self.x * o.y - self.y * o.x)

    def dot(self, o):
        return self.x * o.x + self.y * o.y + self.z * o.z

    def distanceTo(self, o):
        return (self - o).Length

    def _pnt(self):
        return gp_Pnt(self.x, self.y, self.z)

    def _vec(self):
        return gp_Vec(self.x, self.y, self.z)


def _V(v):
    """Chấp nhận Vector hoặc tuple."""
    if isinstance(v, Vector):
        return v
    if isinstance(v, (tuple, list)):
        return Vector(*v)
    raise TypeError("Cần Vector hoặc tuple, nhận %r" % (v,))


# =============================================================================
# Shape
# =============================================================================
class BoundBox(object):
    def __init__(self, box):
        self._b = box

    def _get(self):
        return self._b.Get()

    @property
    def XMin(self):
        return self._get()[0]

    @property
    def YMin(self):
        return self._get()[1]

    @property
    def ZMin(self):
        return self._get()[2]

    @property
    def XMax(self):
        return self._get()[3]

    @property
    def YMax(self):
        return self._get()[4]

    @property
    def ZMax(self):
        return self._get()[5]

    @property
    def XLength(self):
        return self.XMax - self.XMin

    @property
    def YLength(self):
        return self.YMax - self.YMin

    @property
    def ZLength(self):
        return self.ZMax - self.ZMin

    def __repr__(self):
        return ("BoundBox (%.3f, %.3f, %.3f) → (%.3f, %.3f, %.3f)"
                % (self.XMin, self.YMin, self.ZMin, self.XMax, self.YMax, self.ZMax))


class Shape(object):
    def __init__(self, s):
        self._s = s
        if self._s is None:
            raise ValueError("Shape nhận TopoDS_Shape = None")

    # ---------- thông tin ----------
    @property
    def Shape(self):
        return self._s

    @property
    def Volume(self):
        p = GProp_GProps()
        BRepGProp.VolumeProperties_s(self._s, p)
        return p.Mass()

    @property
    def BoundBox(self):
        b = Bnd_Box()
        BRepBndLib.Add_s(self._s, b, True)
        return BoundBox(b)

    @property
    def Solids(self):
        out = []
        ex = TopExp_Explorer(self._s, TopAbs_SOLID)
        while ex.More():
            out.append(Shape(TopoDS.Solid_s(ex.Current())))
            ex.Next()
        return out

    def isValid(self):
        return BRepCheck_Analyzer(self._s).IsValid()

    def isNull(self):
        return self._s.IsNull()

    # ---------- tạo khối ----------
    def extrude(self, direction, length=None):
        d = _V(direction)
        if length is not None:
            d = d.normalized() * length
        return Shape(BRepPrimAPI_MakePrism(self._s, d._vec()).Shape())

    # ---------- boolean ----------
    def _binop(self, other, op):
        o = other.Shape if isinstance(other, Shape) else other
        algo = op(self._s, o)
        algo.Build()
        return Shape(algo.Shape())

    def cut(self, other):
        return self._binop(other, BRepAlgoAPI_Cut)

    def fuse(self, other):
        return self._binop(other, BRepAlgoAPI_Fuse)

    def common(self, other):
        return self._binop(other, BRepAlgoAPI_Common)

    def multiFuse(self, others):
        """Hợp NHẤT nhiều khối thành MỘT khối liền (giống Part.multiFuse của FreeCAD).

        GHI CHÚ KỸ THUẬT: BRepAlgoAPI_BuilderAlgo (general fuse) cho ra đúng THỂ TÍCH
        hợp nhưng giữ các mảnh rời trong compound (vd hợp 2 hộp chồng nhau → 3 solid),
        nên KHÔNG dùng được để kiểm tra "1 khối đặc liền". Ở đây dùng chuỗi
        BRepAlgoAPI_Fuse hai ngôi — kết quả đúng 1 solid khi các khối giao nhau.
        """
        acc = self
        for o in others:
            if o is None:
                continue
            acc = acc.fuse(o)
        return acc

    def removeSplitter(self):
        """Gộp các mặt ĐỒNG PHẲNG/ĐỒNG TRỤC bị chia nhỏ do boolean (giống FreeCAD).

        Cần thiết vì khi hai khối chỉ TIẾP XÚC MẶT (face-to-face) — ví dụ lá bản lề
        áp vào mặt đầu thân vòng — OCCT giữ lại các mặt trùng nhau; bộ tessellate có
        thể sinh vài tam giác diện tích ~0 ở đường may đó. UnifySameDomain hợp nhất
        chúng ⇒ lưới STL sạch, vẫn giữ nguyên hình học/thể tích.
        """
        algo = ShapeUpgrade_UnifySameDomain(self._s, True, True, True)
        algo.Build()
        return Shape(algo.Shape())

    def cutMany(self, others):
        """Cắt một lần với NHIỀU dao (nhanh hơn chuỗi cut rời)."""
        args = TopTools_ListOfShape()
        args.Append(self._s)
        tools = TopTools_ListOfShape()
        for o in others:
            tools.Append(o.Shape if isinstance(o, Shape) else o)
        algo = BRepAlgoAPI_Cut()
        algo.SetArguments(args)
        algo.SetTools(tools)
        algo.SetRunParallel(False)
        algo.Build()
        return Shape(algo.Shape())

    # ---------- biến đổi ----------
    def translate(self, v):
        t = gp_Trsf()
        t.SetTranslation(_V(v)._vec())
        return Shape(BRepBuilderAPI_Transform(self._s, t, True).Shape())

    def rotate(self, center, axis, angle_deg):
        t = gp_Trsf()
        t.SetRotation(gp_Ax1(_V(center)._pnt(), gp_Dir(_V(axis)._vec())),
                      math.radians(angle_deg))
        return Shape(BRepBuilderAPI_Transform(self._s, t, True).Shape())

    def copy(self):
        t = gp_Trsf()
        return Shape(BRepBuilderAPI_Transform(self._s, t, True).Shape())

    # ---------- xuất ----------
    def exportStl(self, path, lin_defl=0.05, ang_defl=0.35):
        mesh = BRepMesh_IncrementalMesh(self._s, lin_defl, False, ang_defl, True)
        mesh.Perform()
        w = StlAPI_Writer()
        w.ASCIIMode = False
        ok = w.Write(self._s, path)
        if not ok:
            raise RuntimeError("Không ghi được STL: %s" % path)
        return ok

    def __repr__(self):
        return "<Shape solid=%d vol=%.2f mm3>" % (len(self.Solids), self.Volume)


# =============================================================================
# Part
# =============================================================================
def makePolygon(points, closed=True):
    mp = BRepBuilderAPI_MakePolygon()
    for p in points:
        p = _V(p)
        mp.Add(gp_Pnt(p.x, p.y, p.z))
    if closed:
        mp.Close()
    mp.Build()
    if not mp.IsDone():
        raise RuntimeError("makePolygon thất bại (đa giác tự cắt?)")
    return Shape(mp.Wire())


def Face(arg, *rest):
    if isinstance(arg, Shape):
        s = arg.Shape
    elif isinstance(arg, (list, tuple)):
        s = makePolygon(arg, closed=True).Shape
    else:
        s = arg
    mf = BRepBuilderAPI_MakeFace(s, True)
    if not mf.IsDone():
        raise RuntimeError("Face thất bại (wire không phẳng/kín?)")
    return Shape(mf.Face())


def makeBox(lx, ly, lz, pos=None, dirn=None):
    pos = _V(pos) if pos is not None else Vector(0, 0, 0)
    mk = BRepPrimAPI_MakeBox(gp_Pnt(pos.x, pos.y, pos.z), float(lx), float(ly), float(lz))
    return Shape(mk.Shape())


def makeCylinder(radius, height, pos=None, dirn=None, angle=360.0):
    pos = _V(pos) if pos is not None else Vector(0, 0, 0)
    if dirn is None:
        mk = BRepPrimAPI_MakeCylinder(float(radius), float(height))
    else:
        d = _V(dirn)
        ax = gp_Ax2(gp_Pnt(pos.x, pos.y, pos.z), gp_Dir(d.x, d.y, d.z))
        mk = BRepPrimAPI_MakeCylinder(ax, float(radius), float(height), math.radians(angle))
        return Shape(mk.Shape())
    return Shape(mk.Shape()).translate(pos)


def makeCone(r1, r2, height, pos=None, dirn=None, angle=360.0):
    pos = _V(pos) if pos is not None else Vector(0, 0, 0)
    mk = BRepPrimAPI_MakeCone(float(r1), float(r2), float(height), math.radians(angle))
    return Shape(mk.Shape()).translate(pos)


def makeCompound(shapes):
    return shapes[0].multiFuse(list(shapes[1:])) if len(shapes) > 1 else shapes[0]


def makeWire(points, closed=False):
    return makePolygon(points, closed=closed)


def show(shape, name=None):
    _doc = ActiveDocument
    if _doc is None:
        _doc = newDocument("Shim")
    obj = _doc.addObject("Part::Feature", name or "Shape")
    obj.Shape = shape
    return obj


# =============================================================================
# App
# =============================================================================
class _ObjProxy(object):
    def __init__(self, name):
        self.Name = name
        self.Label = name
        self.Shape = None


class _DocProxy(object):
    def __init__(self, name):
        self.Name = name
        self.Label = name
        self.Objects = []
        self.saved_to = None

    def addObject(self, typ, name):
        o = _ObjProxy(name)
        self.Objects.append(o)
        return o

    def recompute(self):
        return True

    def saveAs(self, path):
        self.saved_to = path
        # Headless: ghi "sidecar" JSON thay cho .FCStd (không có kernel GUI/WB)
        try:
            import json
            data = {"document": self.Name, "objects": [
                {"name": o.Name,
                 "volume_mm3": round(o.Shape.Volume, 4) if o.Shape else None}
                for o in self.Objects]}
            with open(path + ".json", "w") as f:
                json.dump(data, f, indent=2)
        except Exception:
            pass
        return True


ActiveDocument = None


def newDocument(name="Unnamed"):
    global ActiveDocument
    d = _DocProxy(name)
    ActiveDocument = d
    return d


def closeDocument(name):
    return True


def Version():
    return ("0.21-shim-occt", 0, 0)


class MeshModule(object):
    """`Mesh.export([obj, ...], path)` — như FreeCAD."""

    @staticmethod
    def export(objects, path, tolerance=0.05):
        if not isinstance(objects, (list, tuple)):
            objects = [objects]
        shapes = []
        for o in objects:
            if isinstance(o, Shape):
                shapes.append(o)
            else:
                shapes.append(o.Shape)
        if len(shapes) == 1:
            shapes[0].exportStl(path)
        else:
            comp = makeCompound(shapes)
            comp.exportStl(path)
        return os.path.getsize(path)


# =============================================================================
# Đăng ký module giả vào sys.modules
# =============================================================================
import sys
import types as _types


def install():
    """Gọi hàm này TRƯỚC khi exec các script build_*.py."""
    app_mod = _types.ModuleType("FreeCAD")
    for k, v in list(globals().items()):
        if k.startswith("_"):
            continue
        setattr(app_mod, k, v)
    app_mod.Vector = Vector
    app_mod.ActiveDocument = None
    app_mod.newDocument = newDocument
    app_mod.Version = Version

    part_mod = _types.ModuleType("Part")
    for k in ("makePolygon", "Face", "makeBox", "makeCylinder", "makeCone",
              "makeCompound", "makeWire", "show", "Shape", "Vector", "BoundBox",
              "makeLine"):
        if k in globals():
            setattr(part_mod, k, globals()[k])
    part_mod.makeLine = lambda a, b: makePolygon([_V(a), _V(b)], closed=False)

    mesh_mod = _types.ModuleType("Mesh")
    mesh_mod.export = MeshModule.export

    sys.modules["FreeCAD"] = app_mod
    sys.modules["Part"] = part_mod
    sys.modules["Mesh"] = mesh_mod
    return app_mod, part_mod, mesh_mod
