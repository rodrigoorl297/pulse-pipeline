from __future__ import annotations

from collections import Counter
from pathlib import Path
import json
from statistics import mean


def load_rows(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def metrics(rows: list[dict]) -> dict:
    values = [int(row["value"]) for row in rows]
    return {
        "count": len(rows),
        "avg": round(mean(values), 2),
        "max": max(values),
        "by_status": dict(Counter(row["status"] for row in rows)),
    }


def render_report(stats: dict, domain: str) -> str:
    status_lines = "\n".join(f"- `{k}`: {v}" for k, v in stats["by_status"].items())
    return (
        f"# Relatorio\n\nDominio: **{domain}**\n\n"
        f"- registros: {stats['count']}\n"
        f"- media: {stats['avg']}\n"
        f"- maximo: {stats['max']}\n\n"
        f"## Status\n{status_lines}\n"
    )


def run(source: Path, output: Path, domain: str) -> dict:
    stats = metrics(load_rows(source))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_report(stats, domain), encoding="utf-8")
    return stats
