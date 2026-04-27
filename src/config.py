import os

from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
RETRIEVAL_TOP_K = int(os.getenv("RETRIEVAL_TOP_K", "8"))
RETRIEVAL_DISTANCE_MAX = float(os.getenv("RETRIEVAL_DISTANCE_MAX", "1.0"))
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")
MOCK_DATA_DIR = os.getenv("MOCK_DATA_DIR", "./docs/mock_data")
LOG_DIR = os.getenv("LOG_DIR", "./logs")
COLLECTION_NAME = "px_knowledge"
CHUNK_MAX_TOKENS = 500
CHUNK_OVERLAP_TOKENS = 50
MEMORY_MAX_TURNS = 10
MODEL_NAME = "claude-haiku-4-5"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
