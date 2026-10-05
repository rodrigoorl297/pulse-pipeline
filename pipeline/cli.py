from pathlib import Path

from pipeline.transform import run


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    stats = run(root / "data" / "source.json", root / "output" / "report.md", "edtech")
    print(stats)


if __name__ == "__main__":
    main()
