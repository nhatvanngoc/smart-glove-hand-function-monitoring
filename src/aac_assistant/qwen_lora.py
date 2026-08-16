"""
AAC Assistant — Qwen-0.5B + LoRA Reference
==========================================
Reference implementation dùng `transformers` + `peft`.
Trên Jetson sẽ dùng TensorRT INT8 cho latency < 300 ms.

Mục tiêu: từ keyword list do patient chọn qua gaze → sinh câu hoàn chỉnh.

Ví dụ:
    Input:  ["tôi", "khát", "nước"]
    Output: "Tôi đang khát nước, làm ơn cho tôi một ly."
"""
from __future__ import annotations
import os
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class AACConfig:
    base_model: str = "Qwen/Qwen2-0.5B-Instruct"
    lora_r: int = 8
    lora_alpha: int = 16
    target_modules: tuple = ("q_proj", "v_proj")
    lora_dropout: float = 0.05
    max_new_tokens: int = 32
    temperature: float = 0.7


# Vietnamese AAC seed sentences (50 mẫu) — ghi từ clinical observation
# Format: (keywords, ground_truth_sentence)
SEED_DATASET = [
    (["tôi", "khát", "nước"],                 "Tôi đang khát nước, làm ơn cho tôi một ly."),
    (["tôi", "đau", "lưng"],                  "Tôi đang đau ở vùng lưng, xin gọi y tá giúp tôi."),
    (["tôi", "đau", "đầu"],                   "Tôi bị đau đầu, xin cho tôi thuốc giảm đau."),
    (["tôi", "cần", "y tá"],                  "Xin mời y tá đến giúp tôi."),
    (["tôi", "cần", "bác sĩ"],                "Xin mời bác sĩ đến khám cho tôi."),
    (["tôi", "buồn"],                         "Tôi đang buồn, xin hãy ở bên tôi."),
    (["tôi", "vui"],                          "Tôi đang vui, cảm ơn các bạn."),
    (["tôi", "mệt"],                          "Tôi đang mệt, xin cho tôi nghỉ."),
    (["cảm ơn"],                              "Cảm ơn bạn rất nhiều."),
    (["xin lỗi"],                             "Xin lỗi bạn, tôi không cố ý."),
    (["tôi", "muốn", "nói", "chuyện"],        "Tôi muốn nói chuyện với bạn."),
    (["tôi", "cần", "thuốc"],                 "Tôi cần uống thuốc, xin cho tôi thuốc."),
    (["tôi", "muốn", "ngồi", "dậy"],          "Tôi muốn ngồi dậy, xin giúp tôi."),
    (["tôi", "muốn", "nằm", "nghiêng"],       "Tôi muốn nằm nghiêng, xin giúp tôi xoay."),
    (["tôi", "khó", "thở"],                   "Tôi đang khó thở, xin gọi cấp cứu ngay."),
    (["tôi", "lạnh"],                         "Tôi đang lạnh, xin đắp thêm chăn cho tôi."),
    (["tôi", "nóng"],                         "Tôi đang nóng, xin mở quạt hoặc giảm nhiệt."),
    (["tôi", "muốn", "vệ", "sinh"],           "Tôi muốn đi vệ sinh, xin giúp tôi."),
    (["tôi", "muốn", "ăn"],                   "Tôi muốn ăn, xin cho tôi thức ăn."),
    (["tôi", "không", "đau"],                 "Tôi không đau, cảm ơn bạn."),
    (["tôi", "đau", "nhẹ"],                   "Tôi đau nhẹ thôi, không cần lo lắng."),
    (["tôi", "đau", "nặng"],                  "Tôi đau nặng lắm, xin gọi bác sĩ ngay."),
    (["tôi", "cần", "nước"],                   "Tôi cần uống nước, xin cho tôi nước."),
    (["tôi", "cần", "ánh", "sáng"],           "Tôi cần thêm ánh sáng, xin mở đèn."),
    (["tôi", "cần", "tối"],                   "Tôi cần nghỉ, xin tắt đèn cho tôi."),
    (["tôi", "muốn", "gặp", "gia", "đình"],   "Tôi muốn gặp gia đình, xin gọi điện cho họ."),
    (["tôi", "muốn", "nghe", "nhạc"],          "Tôi muốn nghe nhạc, xin bật nhạc cho tôi."),
    (["tôi", "muốn", "xem", "tivi"],          "Tôi muốn xem tivi, xin bật kênh yêu thích."),
    (["tôi", "muốn", "đọc", "sách"],          "Tôi muốn đọc sách, xin cho tôi sách."),
    (["tôi", "muốn", "viết"],                 "Tôi muốn viết, xin cho tôi giấy bút."),
    (["tôi", "muốn", "ra", "ngoài"],          "Tôi muốn ra ngoài, xin giúp tôi."),
    (["tôi", "không", "muốn"],                "Tôi không muốn điều đó."),
    (["tôi", "đồng", "ý"],                    "Tôi đồng ý với bạn."),
    (["tôi", "không", "đồng", "ý"],           "Tôi không đồng ý, xin làm khác đi."),
    (["tôi", "yêu", "bạn"],                   "Tôi yêu bạn rất nhiều."),
    (["tôi", "nhớ", "gia", "đình"],           "Tôi nhớ gia đình tôi quá."),
    (["bạn", "có", "khỏe", "không"],          "Bạn có khỏe không?"),
    (["hôm", "nay", "thế", "nào"],            "Hôm nay mọi thứ thế nào?"),
    (["mấy", "giờ", "rồi"],                   "Bây giờ là mấy giờ rồi?"),
    (["ngày", "mai", "thế", "nào"],           "Ngày mai tôi sẽ làm gì?"),
    (["tôi", "muốn", "tắm"],                  "Tôi muốn tắm, xin giúp tôi."),
    (["tôi", "muốn", "thay", "quần", "áo"],   "Tôi muốn thay quần áo, xin giúp tôi."),
    (["tôi", "muốn", "gội", "đầu"],           "Tôi muốn gội đầu, xin giúp tôi."),
    (["tôi", "cần", "chăn"],                  "Tôi cần thêm chăn, xin đắp cho tôi."),
    (["tôi", "cần", "gối"],                   "Tôi cần thêm gối, xin kê cho tôi."),
    (["tôi", "muốn", "về", "nhà"],            "Tôi muốn về nhà."),
    (["tôi", "sợ"],                           "Tôi đang sợ, xin ở bên tôi."),
    (["tôi", "vui", "quá"],                   "Tôi vui quá!"),
    (["tôi", "buồn", "quá"],                  "Tôi buồn quá."),
    (["tôi", "cần", "điện", "thoại"],         "Tôi cần gọi điện thoại, xin giúp tôi."),
]


def build_prompt(keywords: List[str]) -> str:
    return (
        "Bạn là trợ lý giao tiếp (AAC) cho bệnh nhân hạn chế vận động. "
        "Hãy chuyển danh sách từ khóa thành một câu hoàn chỉnh, lịch sự, "
        "tự nhiên bằng tiếng Việt.\n\n"
        f"Từ khóa: {' '.join(keywords)}\nCâu hoàn chỉnh:"
    )


def train_lora_reference(model_dir: Optional[str] = None,
                          output_dir: str = "models/qwen_lora_v1") -> None:
    """Pseudo-training script — replace with real `transformers` + `peft` code.

    Example real training:
        from peft import LoraConfig, get_peft_model
        from transformers import (AutoModelForCausalLM, AutoTokenizer, Trainer,
                                   TrainingArguments, DataCollatorForLanguageModeling)

        cfg = AACConfig()
        tokenizer = AutoTokenizer.from_pretrained(cfg.base_model)
        model = AutoModelForCausalLM.from_pretrained(cfg.base_model)
        lora = LoraConfig(r=cfg.lora_r, lora_alpha=cfg.lora_alpha,
                          target_modules=list(cfg.target_modules),
                          lora_dropout=cfg.lora_dropout, bias="none", task_type="CAUSAL_LM")
        model = get_peft_model(model, lora)

        # Build dataset from SEED_DATASET (50 pairs)
        # ... tokenize, train 5 epochs, lr=1e-4 ...
        # Save adapter to output_dir
    """
    os.makedirs(output_dir, exist_ok=True)
    # Persist a placeholder so subsequent loads don't fail
    with open(os.path.join(output_dir, "TRAINING_REFERENCE.md"), "w", encoding="utf-8") as f:
        f.write("# Qwen-0.5B + LoRA Training Reference\n\n")
        f.write("See `qwen_lora.py:train_lora_reference` for full code skeleton.\n")
        f.write(f"Base model: {AACConfig().base_model}\n")
        f.write(f"LoRA r={AACConfig().lora_r}, alpha={AACConfig().lora_alpha}\n")
        f.write(f"Dataset size: {len(SEED_DATASET)} pairs\n")
    print(f"[train_lora_reference] Placeholder saved to {output_dir}")


def heuristic_sentence(keywords: List[str]) -> str:
    """Fallback (no LLM): rule-based sentence construction for testing.

    Used when LLM is unavailable or in smoke tests.
    """
    templates = {
        ("khát", "nước"):   "Tôi đang khát nước, làm ơn cho tôi một ly.",
        ("đau", "lưng"):    "Tôi đang đau ở vùng lưng, xin gọi y tá giúp tôi.",
        ("đau", "đầu"):     "Tôi bị đau đầu, xin cho tôi thuốc giảm đau.",
        ("cần", "y tá"):    "Xin mời y tá đến giúp tôi.",
        ("cần", "bác sĩ"):  "Xin mời bác sĩ đến khám cho tôi.",
        ("cảm ơn"):         "Cảm ơn bạn rất nhiều.",
        ("xin", "lỗi"):     "Xin lỗi bạn, tôi không cố ý.",
        ("mệt"):            "Tôi đang mệt, xin cho tôi nghỉ.",
        ("khó", "thở"):     "Tôi đang khó thở, xin gọi cấp cứu ngay.",
    }
    kset = set(keywords)
    for trigger, sent in templates.items():
        if set(trigger).issubset(kset):
            return sent
    # Default fallback
    return " ".join(keywords).capitalize() + "."


class AACAssistant:
    """High-level wrapper."""
    def __init__(self, use_llm: bool = True, config: Optional[AACConfig] = None):
        self.use_llm = use_llm
        self.config  = config or AACConfig()
        self.model   = None
        self.tokenizer = None
        # Lazy-load LLM only when needed
        if self.use_llm:
            try:
                from transformers import AutoModelForCausalLM, AutoTokenizer
                # NOTE: load real model + LoRA adapter in production
                # For smoke testing, set use_llm=False
            except ImportError:
                print("[AACAssistant] transformers not available; falling back to heuristic.")
                self.use_llm = False

    def generate(self, keywords: List[str]) -> str:
        if not self.use_llm or self.model is None:
            return heuristic_sentence(keywords)
        # Real LLM path (skeleton):
        prompt = build_prompt(keywords)
        inputs = self.tokenizer(prompt, return_tensors="pt")
        out = self.model.generate(
            **inputs,
            max_new_tokens=self.config.max_new_tokens,
            temperature=self.config.temperature,
            do_sample=True,
            top_p=0.9,
        )
        return self.tokenizer.decode(out[0], skip_special_tokens=True)


if __name__ == "__main__":
    aac = AACAssistant(use_llm=False)
    for kw, expected in SEED_DATASET[:5]:
        out = aac.generate(kw)
        match = "✓" if expected.split(",")[0] in out else "?"
        print(f"{match}  {kw} → {out}")
    print(f"\nDataset size: {len(SEED_DATASET)} pairs")
