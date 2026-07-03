from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "properties.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "property_knowledge_base.csv"
DB_PATH = BASE_DIR / "data" / "realestate.db"
