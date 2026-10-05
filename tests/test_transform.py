from pathlib import Path

from pipeline.transform import metrics, run


def test_metrics_and_report(tmp_path: Path):
    source = Path("data/source.json")
    out = tmp_path / "report.md"
    stats = run(source, out, "education")
    assert stats["count"] == 12
    assert "media" in out.read_text(encoding="utf-8")
    assert metrics([{"value": 10, "status": "a"}, {"value": 20, "status": "b"}])["avg"] == 15
