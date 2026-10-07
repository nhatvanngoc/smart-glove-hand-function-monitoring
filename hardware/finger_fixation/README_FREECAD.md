# Chạy bộ sinh STL trong FREECAD (bản thật)

> **Áp dụng cho:** `hardware/finger_fixation/build_idea1_toggle_clasp.py` (Ý tưởng 1 —
> **Cơ cấu đòn bẩy kẹp bên sườn / Side Toggle Clasp**, bản ưu tiên),
> `build_idea2_ratchet_cinch.py` (Ý tưởng 2), `build_idea3_wrap_band.py` (Ý tưởng 3).
> **Bằng chứng kiểm chứng:** `reports/idea1_verify_log.txt`, `idea2_verify_log.txt`,
> `idea3_verify_log.txt`, `reports/freecad_api_audit.txt`, `reports/mesh_qa_log.txt`.

---

## 1. Chạy nhanh nhất (một lệnh, trong FreeCAD)

**Cách A — dòng lệnh (khuyến nghị cho CI / máy có FreeCAD không GUI):**

```bash
freecadcmd <ĐƯỜNG_DẪN>/hardware/finger_fixation/run_in_freecad.py
```

**Cách B — FreeCAD GUI:**

1. Mở FreeCAD → `View → Panels → Python console`.
2. Dán **một dòng** (sửa `<ĐƯỜNG_DẪN>` cho đúng máy bạn):

```python
exec(open(r"<ĐƯỜNG_DẪN>/hardware/finger_fixation/run_in_freecad.py").read())
```

hoặc: `Macro → Macros… → Create` → dán nội dung `run_in_freecad.py` → `Execute`.

**Cách C — chỉ chạy Ý tưởng 1 (bộ ưu tiên):**

```python
exec(open(r"<ĐƯỜNG_DẪN>/hardware/finger_fixation/build_idea1_toggle_clasp.py").read())
```

### Kết quả

```
hardware/finger_fixation/stl/idea1/{Ring_PETG, Pad1_TPU, Pad2_TPU, Pad3_TPU, Pad4_TPU}.stl
hardware/finger_fixation/stl/idea2/{Ring_PETG, Pad1..4_TPU}.stl
hardware/finger_fixation/stl/idea3/{Ring_PETG, Band_TPU, Wedge_PETG}.stl
```

Kèm bảng kiểm PASS/FAIL giống hệt bản chạy tự động (Ý tưởng 1: 13 mục; Ý tưởng 2/3:
11 mục mỗi bên).

---

## 2. Script dùng API nào (và vì sao chạy được trong FreeCAD thật)

Ba script build **chỉ** dùng API FreeCAD chuẩn, có từ bản 0.19 — không dùng API riêng
của bộ kiểm tự động:

| API dùng | Nơi phát sinh | Ghi chú |
|---|---|---|
| `App.Vector(x, y, z)` | dựng điểm | — |
| `Part.makePolygon(points, True)` | `ring_common.prism`, `rad_prism` | ⚠️ tham số `closed` phải truyền **theo vị trí** (xem §3) |
| `Part.Face(wire)` → `.extrude(App.Vector(0,0,h))` | dựng lăng trụ | in không cần support (mọi khối là lăng trụ theo Z) |
| `Part.makeCylinder(r, h, pnt, dir)` | lỗ vít M3 | — |
| `shape.cut(other)` / `fuse` / `common` | boolean | ⚠️ **chỉ một đối tượng** mỗi lần (xem §3) |
| `shape.removeSplitter()` | làm sạch mặt | hợp nhất mặt đồng phẳng do boolean để lại |
| `shape.isValid()`, `.Volume`, `.BoundBox`, `.Solids` | mục kiểm | — |
| `App.newDocument()` → `doc.addObject("Part::Feature", name)` → `o.Shape = shape` → `doc.recompute()` | đăng ký đối tượng | — |
| `Mesh.export([obj], path)` | xuất STL | nhận **danh sách** đối tượng tài liệu |

---

## 3. Ba cái bẫy đã sửa để chạy được trong FreeCAD thật

Bộ kiểm tự động (`headless/`) chạy trên **cùng nhân hình học OCCT** mà FreeCAD dùng,
nhưng trước đây lớp mô phỏng có 3 điểm *dễ dãi hơn FreeCAD* ⇒ script PASS tự động mà
vẫn lỗi khi dán vào FreeCAD. Đã sửa cả hai phía (script + lớp mô phỏng) và thêm bộ rà
soát để không tái phạm:

1. **`shape.cut([a, b, c])` — SAI.** FreeCAD 0.19–1.0 chỉ parse **một** TopoShape:
   `src/Mod/Part/App/TopoShapePyImp.cpp` → `PyArg_ParseTuple(args, "O!", …)`; danh
   sách sẽ `TypeError`. Nay mọi phép cắt nhiều dao dùng `cut_all(shape, [...])`
   (lặp `shape = shape.cut(t)`) hoặc chuỗi `.cut(...).cut(...)`.
2. **`Part.makePolygon(pts, closed=True)` — SAI.** `makePolygon` là *varargs method*
   (`add_varargs_method`), **không nhận keyword** ⇒ `TypeError`. Nay truyền theo vị
   trí: `Part.makePolygon(pts, True)`.
3. **`shape.multiFuse([...])` gây kết quả KHÁC nhau.** Trong FreeCAD `multiFuse` là
   **general fuse** (`BRepAlgoAPI_BuilderAlgo`) nên có thể trả về *compound nhiều mảnh
   rời* — mục kiểm “1 khối liền” sẽ báo sai. Nay mọi phép hợp dùng `fuse_chain(...)`
   (chuỗi `fuse` hai ngôi) ⇒ luôn đúng 1 solid khi các khối ngập nhau ≥ 0,05 mm.
   *Đã đồng bộ lớp mô phỏng:* `freecad_compat.py` nay cũng dùng general fuse cho
   `multiFuse`, từ chối danh sách ở `cut/fuse/common`, và **đã bỏ** `cutMany`
   (hàm này không tồn tại trong FreeCAD).

Ngoài ra `sys.exit()` trong script được bọc bằng biến `FF_NO_SYS_EXIT` (đặt tự động bởi
`run_in_freecad.py`): trong FreeCAD **GUI**, `sys.exit()` ném `SystemExit` và có thể
**đóng ứng dụng**.

---

## 4. Kiểm tra lại tính tương thích (không cần chạy dựng hình)

```bash
python headless/freecad_api_audit.py --write     # ngoài FreeCAD: đối chiếu danh sách trắng
freecadcmd headless/freecad_api_audit.py         # TRONG FreeCAD: hasattr() thật
```

Bộ rà soát bắt: danh sách truyền cho `cut/fuse/common`, keyword của `makePolygon`,
`multiFuse`, `cutMany`, `sys.exit` (cảnh báo) — và tự kiểm bằng 7 mẫu mã ĐÚNG/SAI
(xem `reports/freecad_api_audit.txt`).

---

## 5. Không có FreeCAD vẫn kiểm tra được (headless)

Máy chủ/CI không cài FreeCAD vẫn chạy được **cùng** ba script nhờ lớp tương thích
`headless/freecad_compat.py` (OCCT thật, API FreeCAD giả lập):

```bash
bash headless/bootstrap_env.sh          # tạo ~/.tooling/venv + ~/.tooling/py (một lần)
~/.tooling/py headless/run_verify.py    # 3/3 script PASS (13 + 11 + 11 mục)
~/.tooling/py headless/mesh_qa.py       # 13 STL: kín, 1 mảnh, 0 tam giác suy biến
```

> **Tính trung thực của hai đường chạy:** lớp mô phỏng dùng *cùng* `OCP` (OCCT 7.9.3)
> mà FreeCAD liên kết, và đã được chỉnh để **từ chối** đúng những gì FreeCAD từ chối.
> Khác biệt tiềm ẩn còn lại: FreeCAD có thể tessellate lưới với sai số khác (mặc định
> `0,1 mm`/`28,5°`) ⇒ số tam giác trong STL có thể chênh, còn **hình học và thể tích
> B-Rep thì không đổi**. Mọi số trong báo cáo là **ngân sách thiết kế**, không phải kết
> quả đo hay chế tạo.

---

## 6. In thử (kinh nghiệm, chưa kiểm chứng bằng mẫu in)

* Vật liệu: khung `PETG`; đệm/đai `TPU 85A` (và `TPU 95A` cho đệm Ý tưởng 1–2).
* Nozzle 0,4 mm; lớp 0,16–0,20 mm; **tắt gap-fill** để giữ khe 0,45 mm và các rãnh
  0,10 mm (nếu slicer lấp khe, cơ cấu sẽ bị “hàn” khi in).
* Cầu in cho khe 0,45 mm: in theo phương Z (mọi khối là lăng trụ theo Z) nên khe là
  *khe dọc*, không cần support.
* Đệm TPU in rời rồi lắp vào rãnh chữ T trên vòng (rãnh đã chừa 0,10 mm mọi phía).
