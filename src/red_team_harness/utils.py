import os
import json
from typing import Any, Dict, List, Tuple
from datetime import datetime
import uuid


def _append(messages, role: str, content: str):
    entry = {"role": role, "content": content}
    messages.append(entry)
    border = "=" * 50
    print(f"\n{border} {role.upper()} {border}\n{content.strip()}\n")
    return messages


def run_dir(base: str, prefix: str = "run") -> str:
    """
    Name format: {prefix}{nn}-{YYYYmmdd-HHMMSS}-{shortuuid}
    Example: run01-20250823-013045-a1b2c3d4
    """
    os.makedirs(base, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    short = str(uuid.uuid4())[:8]
    existing = [
        d
        for d in os.listdir(base)
        if d.startswith("run") and os.path.isdir(os.path.join(base, d))
    ]
    idx = len(existing) + 1
    name = f"{prefix}{idx:02d}-{ts}-{short}"
    path = os.path.join(base, name)
    os.makedirs(path, exist_ok=True)
    return path
