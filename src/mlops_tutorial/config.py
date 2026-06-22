# import library to use
from pathlib import Path

# Root directory
ROOT_DIR = Path(__file__).resolve().parents[2]

# Data folder
DATA_DIR = ROOT_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Dataset file
RAW_DATA_FILE = RAW_DATA_DIR / "Telco-Customer-Churn.csv"

TRAIN_FILE = PROCESSED_DATA_DIR / "train.csv"
TEST_FILE = PROCESSED_DATA_DIR / "test.csv"
