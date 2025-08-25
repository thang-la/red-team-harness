from dataclasses import dataclass


@dataclass
class ModelConfig:
    model: str = "openai/gpt-oss-20b"


@dataclass
class RunConfig:
    out_dir: str = "findings"
    temperature: float = 1.0
    top_p: float = 1.0
