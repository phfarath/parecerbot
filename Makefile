.PHONY: setup ingest run clean

setup:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt
	cp -n .env.example .env || true
	@echo "Configure ANTHROPIC_API_KEY no arquivo .env"

ingest:
	. .venv/bin/activate && python -m src.ingest

run:
	. .venv/bin/activate && streamlit run src/app.py --server.port 8501 --server.fileWatcherType none

clean:
	rm -rf chroma_db/
	rm -f logs/queries.jsonl
	@echo "Indice e logs removidos"
