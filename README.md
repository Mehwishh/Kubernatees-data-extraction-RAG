# Production RAG

Python 3.11+ scaffold for a FastAPI RAG service using LangGraph, Portkey,
NeMo Guardrails, Gemini embeddings, Qdrant, and FlashRank. The API and provider
modules are scaffolding; `/query` intentionally returns `503` until the guarded
RAG workflow is configured.

## Windows setup (PowerShell)

The workspace virtual environment is `.venv`.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell blocks activation, call the environment interpreter directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

Copy `.env.example` to `.env` and add credentials for the services you configure.
Do not commit `.env` or real credentials.

## Layout

```text
app/
  agents/nodes/       LangGraph planner, retriever, and responder
  gateway/            Portkey model routing
  guardrails/         NeMo Guardrails input/output boundary
  ingestion/
    chunking/         Paragraph-aware 1,500-character chunks
    loaders/          PDF, HTML, TXT, DOCX, and PPTX loader modules
  services/retrieval/ Gemini embeddings, Qdrant search, and FlashRank reranking
  config.py           Environment-based settings
  main.py             FastAPI entrypoint and /query endpoint
evals/                RAGAS evaluation entrypoint
ui/                   Streamlit chat UI entrypoint
processed_data/       Generated parsed/chunked document output
docs/                 11 architecture and operations guides
DATA/
  true/               True/grounded sample-document inputs
  noisy/              Noisy sample-document inputs
requirements.txt      Runtime dependency manifest
```

`processed_data/` is generated output and should not be used as source data.
Keep the sample dataset directories free of private or licensed material.
