import argparse
from .config import ModelConfig, RunConfig
from .harness import run
from .utils import run_dir


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="ollama-harness", description="Red Team Harness for LLMs"
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    runp = sub.add_parser("run", help="Run a scripted task")
    runp.add_argument(
        "--task",
        default="reward_hacking",
        choices=["reward_hacking"],
        help="Task to run",
    )
    runp.add_argument("--model", default="openai/gpt-oss-20b", help="Model")
    runp.add_argument("--out", dest="out_dir", default="findings")
    runp.add_argument(
        "--temperature", type=float, default=1.0, help="Sampling temperature"
    )
    runp.add_argument("--top-p", type=float, default=1.0, help="Nucleus sampling top-p")
    runp.add_argument(
        "--repeat", type=int, default=1, help="Number of times to run the task"
    )
    return p


def main():
    parser = build_parser()
    args = parser.parse_args()

    model_cfg = ModelConfig(model=args.model)
    run_cfg = RunConfig(
        out_dir=args.out_dir,
        temperature=args.temperature,
        top_p=args.top_p,
    )

    if args.cmd == "run":
        for i in range(max(1, args.repeat)):
            dir = run_dir(args.out_dir, prefix=f"run{i+1:02d}-")
            run_cfg.out_dir = dir
            meta = run(
                model_cfg,
                run_cfg,
                args.task,
            )
            print(f"\nArtifacts (run {i+1}/{args.repeat}):", meta["artifacts"])


if __name__ == "__main__":
    main()
