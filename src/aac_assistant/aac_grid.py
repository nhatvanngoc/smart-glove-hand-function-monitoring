"""
AAC Grid + Gaze-driven Selection
================================
Mô phỏng grid 5×3 (15 ô từ vựng) cho patient chọn bằng gaze dwell-time.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Tuple, Optional


@dataclass
class AACCell:
    word: str
    pos: Tuple[int, int]            # (row, col)
    dwell_ms: int = 0
    selected: bool = False


@dataclass
class AACGrid:
    rows: int = 3
    cols: int = 5
    dwell_threshold_ms: int = 800
    cells: List[AACCell] = field(default_factory=list)
    selected_words: List[str] = field(default_factory=list)

    def __post_init__(self):
        words = [
            ["Tôi", "Bạn", "Cần", "Muốn", "Xin"],
            ["Cảm ơn", "Xin lỗi", "Vui", "Buồn", "Mệt"],
            ["Nước", "Thuốc", "Đau", "Y tá", "Bác sĩ"],
        ]
        if not self.cells:
            self.cells = []
            for r in range(self.rows):
                for c in range(self.cols):
                    self.cells.append(AACCell(word=words[r][c], pos=(r, c)))

    def hit_test(self, gaze_xy: Tuple[float, float], grid_origin: Tuple[float, float] = (0.0, 0.0),
                 cell_w: float = 100.0, cell_h: float = 100.0) -> Optional[AACCell]:
        """Determine which cell gaze is on.

        gaze_xy: (x, y) in pixels
        returns: AACCell or None
        """
        gx, gy = gaze_xy
        ox, oy = grid_origin
        for cell in self.cells:
            r, c = cell.pos
            x0 = ox + c * cell_w
            y0 = oy + r * cell_h
            if x0 <= gx < x0 + cell_w and y0 <= gy < y0 + cell_h:
                return cell
        return None

    def update(self, gaze_xy: Tuple[float, float], dt_ms: int = 33) -> Optional[str]:
        """Tick: dwell-time accumulation, select on threshold.

        Returns newly selected word, or None.
        """
        cell = self.hit_test(gaze_xy)
        for c in self.cells:
            if c is cell:
                c.dwell_ms += dt_ms
                if c.dwell_ms >= self.dwell_threshold_ms and not c.selected:
                    c.selected = True
                    self.selected_words.append(c.word)
                    # reset dwell after selection
                    for cc in self.cells:
                        cc.dwell_ms = 0
                        cc.selected = False
                    return c.word
            else:
                c.dwell_ms = max(0, c.dwell_ms - dt_ms * 2)  # decay fast
        return None

    def reset(self) -> None:
        self.selected_words.clear()
        for c in self.cells:
            c.dwell_ms = 0
            c.selected = False

    def get_keywords(self) -> List[str]:
        return list(self.selected_words)


if __name__ == "__main__":
    grid = AACGrid(dwell_threshold_ms=300)  # shorter for test
    # Simulate gaze on cell (2, 2) = "Đau" for 1 second
    cell_w, cell_h = 100, 100
    cx = 50 + 2 * cell_w   # cell col 2
    cy = 50 + 2 * cell_h   # cell row 2
    for tick in range(35):  # 35 ticks @ 33 ms = 1.155 s
        sel = grid.update((cx, cy), dt_ms=33)
        if sel:
            print(f"Tick {tick}: selected → {sel}")
    print("Keywords so far:", grid.get_keywords())
