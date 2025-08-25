import os
from dataclasses import asdict
from typing import Dict, List

from transformers import AutoTokenizer, AutoModelForCausalLM
from .config import ModelConfig, RunConfig
from .utils import _append
from .exporters import export_finding
from .prompts import SAFE_SYSTEM_PROMPT, EXPLOIT_PROMPTS


def run(model_cfg: ModelConfig, run_cfg: RunConfig, task: str) -> Dict:

    tokenizer = AutoTokenizer.from_pretrained(model_cfg.model)
    model = AutoModelForCausalLM.from_pretrained(
        model_cfg.model, torch_dtype="auto", device_map="auto"
    )

    os.makedirs(run_cfg.out_dir, exist_ok=True)

    for idx, item in enumerate(EXPLOIT_PROMPTS[task], start=1):
        messages: List[Dict[str, str]] = []

        _append(messages, "system", SAFE_SYSTEM_PROMPT)
        _append(messages, "user", item["prompt"])

        inputs = tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt",
            return_dict=True,
        ).to(model.device)

        outputs = model.generate(
            **inputs,
            max_new_tokens=20000,
            temperature=run_cfg.temperature,
            top_p=run_cfg.top_p,
        )

        result = tokenizer.decode(outputs[0])
        filename = os.path.join(run_cfg.out_dir, f"finding_{idx}.json")

        export_finding(
            result,
            temperature=run_cfg.temperature,
            top_p=run_cfg.top_p,
            task_name=task,
            behavior=item["behavior"],
            filename=filename,
        )

        print(f"\n✅ The output has been saved at: {filename}")
        print("=" * 80)

    return {
        "model": asdict(model_cfg),
        "run": asdict(run_cfg),
    }
