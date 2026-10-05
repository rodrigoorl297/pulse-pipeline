# Pulse Pipeline

ETL local (JSON -> metricas -> Markdown) para **edtech**. Roda em arquivo; nao envia dado para fora.

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -e ".[dev]"
python -m pipeline.cli
pytest -q
```
