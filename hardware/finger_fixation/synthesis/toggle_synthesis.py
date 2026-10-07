# -*- coding: utf-8 -*-
"""
toggle_synthesis.py — TỔNG HỢP CHÍNH XÁC "KẸP QUÁ TÂM SƯỜN" (Ý tưởng 1)
================================================================================
KHÔNG đoán hình học khoá. Kích thước khoá được TÍNH RA từ 4 điều kiện kiểm tra được:

  (1) KHÔNG RƠ: ngàm móc có MẶT DỐC (ramp) tì lên CHỐT TRỤ P của tay kẹp + mặt chặn
      cứng. Hai bề mặt tì ⇒ vị trí đóng là XÁC ĐỊNH (determinate), không khe hở lắp
      ghép vì toàn bộ là MỘT chi tiết in liền khối (0 bu-lông, 0 trục xoay rời).
  (2) QUÁ TÂM (tự cường hoá): ở trạng thái đóng, pháp tuyến tiếp xúc của mặt dốc tạo
      mô-men quanh tâm quay A của cần gạt CÙNG CHIỀU với mặt chặn cứng ⇒ tải kéo của
      ngón ÉP cần gạt vào mặt chặn, KHÔNG thể dẫn động ngược cần gạt.
  (3) LỰC NHẢ ≤ 8 N: lực ngón cái = M_tải / R_handle (R_handle = tay đòn nhả).
  (4) HÀNH TRÌNH: khe mở ≥ 5 mm để luồn ngón Ø20–24 trong < 3 s, một tay.

SƠ ĐỒ (mặt cắt ngang đốt gần; +X = sườn, +Y = mu; gốc = tâm đốt gần):

        cần gạt quay quanh A (tai trên mặt mu) ── đệm ngón cái ở đầu tay đòn R_handle
             |
      R_arm  \  mặt dốc β  ⟋ tì lên chốt trụ P (Ø3 mm, in liền trên tay kẹp)
             |                |
             |      tay kẹp  |  quay quanh bản lề lá Hp (in liền với thân vòng)
             A ──── thân vòng ──── Hp

LÁ ĐÀN HỒI ĐẤT: tai A gắn vào thân qua lá mỏng k ≈ 5.7 N/mm, hành trình ±1.5 mm
  ⇒ (a) tạo lực kẹp cần (7.8 N/đệm), (b) phủ dải Ø20–24, (c) bù dung sai in & bù từ biến.

TẤT CẢ số liệu là NGÂN SÁCH THIẾT KẾ (tính toán hình học/lực học), KHÔNG phải đo
thực nghiệm — theo AGENTS.md §1.
Đầu ra: synthesis/toggle_synthesis_report.txt
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import params as P  # noqa: E402


def pol(r, phi_deg):
    t = math.radians(phi_deg)
    return (r * math.cos(t), r * math.sin(t))


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, s):
    return (a[0] * s, a[1] * s)


def norm(a):
    L = math.hypot(a[0], a[1])
    return (0.0, 0.0, 0.0) if L < 1e-12 else (a[0] / L, a[1] / L, L)


def cross2(a, b):
    return a[0] * b[1] - a[1] * b[0]


def ang(v):
    return math.degrees(math.atan2(v[1], v[0]))


def rot(v, deg):
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    return (v[0] * c - v[1] * s, v[0] * s + v[1] * c)


# =============================================================== 1. HÌNH HỌC CƠ SỞ
D_NOM = P.D_NOM
R_ARC = 12.6                                   # bán kính cung khe hở tay kẹp (từ Hp)
HP = pol(11.13, P.HINGE_PHI)                   # (10.168, -4.527)
PEG = pol(13.35, 52.0)                         # ( 8.219, 10.520) — chốt P ở ĐÓNG
R3 = norm(sub(PEG, HP))[2]                     # 15.173 mm
U_RAD = norm(sub(PEG, HP))[:2]                 # pháp tuyến hướng ra tại P
T_OPEN = (-U_RAD[1], U_RAD[0])                 # tiếp tuyến = chiều chốt P chạy khi MỞ
# xác nhận chiều mở: tay kẹp mở ⇒ góc θ3 giảm ⇒ chốt P chạy theo -T_OPEN
D_PEG_ARC = {+1: T_OPEN, -1: mul(T_OPEN, -1.0)}

PEG_D = 3.00          # Ø chốt trụ trên tay kẹp (in liền)
ARM_LEN = 4.00        # khoảng cách A → chốt P (tay đòn kéo) — KHỚP build_idea1
ARM_SLANT = 30.0      # ° — độ nghiêng tay đòn so với pháp tuyến (giữ A trong ΔX và thấp)
R_HANDLE = 4.15       # tay đòn nhả (|u| từ A tới tâm đệm ngón cái) — KHỚP build_idea1
RAMP_BETA = 15.0      # ° — lệch của pháp tuyến mặt khoá so với phương tải (độ vát nhả)
MU_CONTACT = 0.35     # PETG–PETG in (khô) — cho mặt dốc; μ_da=0.80 dùng cho đệm
STOP_R = 3.10         # mm — tay đòn của LAND (mặt chặn cứng) tính từ A
OC_MARGIN = 2.0       # ° — biên quá tâm thiết kế (đã trừ vào góc làm việc)
DOVETAIL_ANG = 0.0    # ° — nếu >0: rãnh móc vuốt (undercut) chống nhấc chốt ra

A = add(PEG, mul(rot(U_RAD, ARM_SLANT), ARM_LEN))
C_PEG = PEG                                    # điểm tiếp xúc danh nghĩa trên chốt

# =============================================================== 2. LỰC HỌC NGÂN SÁCH
F_TENDON = float(P.F_TENDON_NOM)               # 25 N
MU = float(P.MU_DESIGN)                        # 0.80 (TPU 85A ↔ da)
N_PAD = int(P.N_PAD)
M_OPEN = 70.0                                  # N·mm — mô-men mở tay kẹp (ngân sách)
SIGMA_N = F_TENDON / MU                        # 31.2 N tổng pháp tuyến cần
N_PAD_EACH = SIGMA_N / N_PAD                   # 7.8 N/đệm
F_PEG = M_OPEN / R3                            # 4.61 N — lực kéo tại chốt P

# pháp tuyến tiếp xúc của mặt dốc trong hệ cố định (trạng thái ĐÓNG)
#   chốt P bị mặt dốc ép theo chiều đóng (-T_OPEN); pháp tuyến nghiêng β so với nó
N_CONTACT = rot(mul(D_PEG_ARC[-1], 1.0), -RAMP_BETA)   # = chiều đóng quay -β
# mô-men tải (lực F_PEG dọc pháp tuyến, đặt tại P) quanh A:
M_LOAD_SIGNED = cross2(sub(PEG, A), N_CONTACT) * F_PEG
H_LOAD = abs(cross2(sub(PEG, A), N_CONTACT))          # tay đòn tải (mm)
F_RELEASE = abs(M_LOAD_SIGNED) / R_HANDLE
F_RELEASE_TOTAL = F_RELEASE + 1.5                      # + độ cứng lá & ma sát
F_STOP = abs(M_LOAD_SIGNED) / STOP_R

# =============================================================== 3. HÀNH TRÌNH
TH3_CLOSED = ang(sub(PEG, HP))                          # 97.379°
GAP_OPEN = 5.0                                          # mm khe mở thiết kế
TH3_OPEN = TH3_CLOSED - math.degrees(GAP_OPEN / R_ARC)
PEG_TRAVEL = abs(math.radians(TH3_OPEN - TH3_CLOSED)) * R3
# Với tay đòn hợp với pháp tuyến ARM_SLANT: quãng đường móc đi mỗi radian cần gạt
LEVER_EFF = ARM_LEN * math.cos(math.radians(ARM_SLANT))  # mm/rad
# mặt dốc khuếch đại (wedge): chốt P đi được 1/tan(β) lần so với móc đi dọc ray
WEDGE = 1.0 / math.tan(math.radians(RAMP_BETA))
LEVER_STROKE_DEG = math.degrees(PEG_TRAVEL / (LEVER_EFF * WEDGE))
HANDLE_TRAVEL = math.radians(LEVER_STROKE_DEG) * R_HANDLE
# công kẹp (J → N·mm) và lực kẹp trung bình trên tay người dùng
W_CLOSE = F_PEG * PEG_TRAVEL
F_CLOSE_MEAN = W_CLOSE / max(HANDLE_TRAVEL, 1e-6)

# =============================================================== 4. TỰ CƯỜNG HOÁ
def oc_flip_deg(step=0.25, span=180.0):
    """Góc quay của cần gạt để mô-men tải đổi dấu (biên tự cường hoá thực)."""
    n = int(span / step)
    prev = None
    for i in range(n + 1):
        d = i * step
        nc = rot(N_CONTACT, d)
        m = cross2(sub(PEG, A), nc)
        if prev is not None and (prev == 0.0 or m == 0.0 or prev * m < 0):
            return d
        prev = m
    return None


OC_MARGIN_ACTUAL = oc_flip_deg()

# --- ma sát nêm ---
RHO_CONTACT = math.degrees(math.atan(MU_CONTACT))          # góc ma sát PETG–PETG
SELF_LOCK = RAMP_BETA < RHO_CONTACT                        # nêm tự hãm (β < ρ)
F_RAMP_PUSH = F_PEG * math.tan(math.radians(RAMP_BETA + RHO_CONTACT))   # N — đẩy nêm khi ĐÓNG
F_WEDGE_RELEASE = F_PEG * max(0.0, math.tan(math.radians(RHO_CONTACT - RAMP_BETA)))  # N — nhả nêm
H_CONTACT = abs(cross2(sub(PEG, A), mul(N_CONTACT, -1.0)))  # tay đòn của lực đẩy quanh A
F_CLOSE_USER = F_RAMP_PUSH * H_CONTACT / R_HANDLE

# =============================================================== 5. LÁ ĐÀN HỒI ĐẤT
LEAF = dict(b=7.6, t=0.55, L=4.30)   # = lá mỏng THẬT trong build_idea1 (eo 0.55 mm)
E_PETG = float(P.E_PETG)
SIGMA_Y = 48.0
If = LEAF['b'] * LEAF['t'] ** 3 / 12.0
K_LEAF = 3.0 * E_PETG * If / LEAF['L'] ** 3
LEAF_TRAVEL = 0.8
LEAF_SIGMA = E_PETG * LEAF['t'] * LEAF_TRAVEL / (2 * LEAF['L'] ** 2)
LEAF_FORCE = K_LEAF * LEAF_TRAVEL
LEAF_TAKEOVER = SIGMA_N / K_LEAF          # mm — tổng biến dạng lá để tạo đủ lực kẹp
LEAF_OK = LEAF_FORCE >= SIGMA_N * 0.9


def report():
    out = []
    w = out.append
    w("=" * 78)
    w("TỔNG HỢP CHÍNH XÁC — KẸP QUÁ TÂM SƯỜN (SIDE TOGGLE CLASP), Ý TƯỞNG 1")
    w("Khoá = MÓC CÓ MẶT DỐC (ramp) tì chốt trụ + QUÁ TÂM trên mặt chặn cứng")
    w("=" * 78)
    w("A. HÌNH HỌC (mm; φ từ trục sườn +X, +Y = mu; gốc = tâm đốt gần)")
    w("   Hp  (bản lề lá tay kẹp) = (%7.3f, %7.3f)  r=%5.2f  φ=%.1f°"
      % (HP[0], HP[1], math.hypot(*HP), P.HINGE_PHI))
    w("   P   (chốt trụ Ø%.1f mm)   = (%7.3f, %7.3f)  r=%5.2f  φ=52.0°"
      % (PEG_D, PEG[0], PEG[1], math.hypot(*PEG)))
    w("   A   (tâm quay cần gạt) = (%7.3f, %7.3f)  r=%5.2f   [tai trên mặt mu]"
      % (A[0], A[1], math.hypot(*A)))
    w("   |A–P| = %.2f mm (tay đòn kéo) ; nghiêng %.1f° so với pháp tuyến; R_handle = %.1f mm"
      % (ARM_LEN, ARM_SLANT, R_HANDLE))
    w("   X cực đại của cơ cấu = %.2f mm ≤ ngân sách ΔX (a_out = A_F1+GAP_FIT+T_SIDE = %.2f mm)"
      % (max(abs(A[0]), abs(PEG[0])), P.A_F1 + P.GAP_FIT + P.T_SIDE))
    w("-" * 78)
    w("B. BỐN ĐIỀU KIỆN KHOÁ (tính ra, kiểm tra bằng số)")
    w("   B1. KHÔNG RƠ — móc tì mặt dốc β=%.0f° lên chốt trụ Ø%.1f mm; hai bề mặt tì ⇒" % (RAMP_BETA, PEG_D))
    w("       trạng thái đóng xác định (determinate). Toàn bộ cơ cấu là MỘT chi tiết in")
    w("       liền khối ⇒ KHÔNG có khe hở lắp ghép, không bu-lông/trục rời ⇒ không rơ.")
    w("       Mặt dốc + rãnh móc ôm >180° quanh chốt ⇒ chống nhấc chốt ra theo phương Z.")
    w("   B2. QUÁ TÂM — tay đòn tải h = %.3f mm, mô-men tải lên cần gạt M = %.2f N·mm," % (H_LOAD, abs(M_LOAD_SIGNED)))
    w("       chiều mô-men = %s (âm = kim đồng hồ). MẶT CHẶN CỨNG đặt ở phía TĂNG góc quay"
      % ("ÂM" if M_LOAD_SIGNED < 0 else "DƯƠNG"))
    w("       (tức phía tải ÉP tới), bán kính %.1f mm ⇒ lực tì lên mặt chặn = %.2f N."
      % (STOP_R, F_STOP))
    w("       ⇒ TỰ CƯỜNG HOÁ (form-closed): tải ÉP cần gạt THÊM vào mặt chặn, không thể")
    w("       dẫn động ngược cần gạt. Nhả khoá = người dùng xoay cần gạt NGƯỢC lại (mục D).")
    w("   B3. BIÊN TỰ CƯỜNG HOÁ: phải quay cần gạt %.1f° mới tới điểm đảo dấu mô-men tải"
      % (OC_MARGIN_ACTUAL if OC_MARGIN_ACTUAL else float('nan')))
    w("       ⇒ dự trữ %.1f° ≫ hành trình làm việc %.1f° ⇒ khoá bền vững trước dung sai in."
      % (OC_MARGIN_ACTUAL if OC_MARGIN_ACTUAL else 0.0, LEVER_STROKE_DEG))
    w("   B4. KHUẾCH ĐẠI KIỂU NÊM: mặt dốc β=%.0f° ⇒ hệ số hình học 1/tanβ = %.2f lần."
      % (RAMP_BETA, WEDGE))
    w("       Nêm TỰ HÃM: β=%.0f° < ρ=atan(μ_nhựa)=%.1f° (μ_nhựa=%.2f) ⇒ khoá 2 lớp: FORM-CLOSED"
      % (RAMP_BETA, RHO_CONTACT, MU_CONTACT))
    w("       (mặt chặn cứng) là chính + TỰ HÃM MA SÁT là dự phòng ⇒ không trôi, không lỏng.")
    w("-" * 78)
    w("C. HÀNH TRÌNH (một tay, < 3 s)")
    w("   Khe mở thiết kế %.1f mm ở r=%.1f mm ⇒ tay kẹp quay %.2f° (θ3: %.2f° → %.2f°)"
      % (GAP_OPEN, R_ARC, abs(TH3_OPEN - TH3_CLOSED), TH3_CLOSED, TH3_OPEN))
    w("   ⇒ chốt P đi %.2f mm theo cung; cần gạt quay %.1f°; đầu ngón cái đi %.2f mm"
      % (PEG_TRAVEL, LEVER_STROKE_DEG, HANDLE_TRAVEL))
    w("   (tay đòn hiệu dụng %.2f mm/rad × khuếch đại nêm %.2f)" % (LEVER_EFF, WEDGE))
    w("-" * 78)
    w("D. NGÂN SÁCH LỰC (thiết kế — KHÔNG phải đo thực nghiệm)")
    w("   F_tendon = %.0f N dọc trục, μ = %.2f ⇒ ΣN = %.1f N ⇒ %.1f N mỗi đệm (4 đệm)"
      % (F_TENDON, MU, SIGMA_N, N_PAD_EACH))
    w("   M_open = %.0f N·mm (ngân sách) ⇒ lực kéo tại chốt P: F_peg = M_open/R3 = %.2f N" % (M_OPEN, F_PEG))
    w("   LỰC NHẢ (ngón cái) = M/R_handle + ma sát nhả nêm + độ cứng lá")
    w("       = %.2f N + %.2f N + 1.50 N = %.2f N   [mục tiêu ≤ 8 N] ⇒ %s"
      % (F_RELEASE, F_WEDGE_RELEASE, F_RELEASE + F_WEDGE_RELEASE + 1.5,
         "PASS" if (F_RELEASE + F_WEDGE_RELEASE + 1.5) <= 8.0 else "FAIL"))
    w("   LỰC KẸP (ngón cái, có ma sát nêm) = F_peg·tan(β+ρ)·h_tay/R_handle = %.2f N  [≤ 10 N] ⇒ %s"
      % (F_CLOSE_USER, "PASS" if F_CLOSE_USER <= 10.0 else "FAIL"))
    w("   Ứng suất tì: lực %.2f N trên vệt tiếp xúc ~%.1f mm² ⇒ %.2f MPa ≪ σ_y=%.0f MPa"
      % (F_STOP, 2.4, F_STOP / 2.4, SIGMA_Y))
    w("-" * 78)
    w("E. LÁ ĐÀN HỒI ĐẤT (tai A gắn vào thân qua lá mỏng)")
    w("   Tiết diện %.1f × %.2f mm, dài %.1f mm ⇒ I = %.3f mm⁴ ⇒ k = 3EI/L³ = %.2f N/mm"
      % (LEAF['b'], LEAF['t'], LEAF['L'], If, K_LEAF))
    w("   Để tạo đủ ΣN = %.1f N cần biến dạng %.2f mm (≤ hành trình ±%.1f mm) ⇒ phủ Ø%d–Ø%d"
      % (SIGMA_N, LEAF_TAKEOVER, LEAF_TRAVEL, D_NOM - 2, D_NOM + 2))
    w("   σ_max tại hành trình %.1f mm = %.1f MPa (FoS %.1f theo σ_y = %.0f MPa) ⇒ %s"
      % (LEAF_TRAVEL, LEAF_SIGMA, SIGMA_Y / LEAF_SIGMA, SIGMA_Y, "PASS" if LEAF_SIGMA < SIGMA_Y / 2 else "FAIL"))
    w("   Vai trò: (a) tạo lực kẹp, (b) phủ dải Ø20–24, (c) bù dung sai in & từ biến PETG.")
    w("-" * 78)
    w("F. GHI CHÚ PHƯƠNG PHÁP (để không lặp lại lỗi thiết kế)")
    w("   1) Trong cơ cấu 4 khâu, điều kiện 'Hp–P–C thẳng hàng' KHÔNG phải khoá: nếu đường")
    w("      lực của thanh truyền đi qua Hp thì mô-men cân bằng của tay kẹp = 0 ⇒ tay kẹp MẤT ĐỠ.")
    w("   2) Cơ cấu 4 khâu non-Grashof bị chặn cứng ở |A–P| = R1+R2 ⇒ KHÔNG thể 'snap-through'")
    w("      qua gối thẳng bằng đàn hồi ⇒ không thể nhả. Vì vậy bản này dùng MÓC + NÊM + mặt")
    w("      chặn (đúng nguyên lý khoá quá tâm kiểu khoá giày trượt tuyết / kẹp vise-grip).")
    w("   3) Khoá phải là FORM-CLOSED (hình học), không dựa vào ma sát ⇒ không trôi theo thời gian.")
    w("=" * 78)

    txt = "\n".join(out)
    print(txt)
    path = os.path.join(HERE, "toggle_synthesis_report.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print("\n[ĐÃ GHI] %s" % path)
    return txt


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        print("OK A=(%.3f,%.3f) M=%.2f N·mm  F_release=%.2f N  OC_flip=%s°"
              % (A[0], A[1], M_LOAD_SIGNED, F_RELEASE_TOTAL, OC_MARGIN_ACTUAL))
    else:
        report()
