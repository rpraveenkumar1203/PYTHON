from __future__ import annotations
import os
from pathlib import Path


DATA_DIR = Path(os.getenv("DATA_DIR", "storage"))
RECEIPTS_DIR = DATA_DIR / "receipts"
XLSX_PATH = DATA_DIR / "data.xlsx"
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")  # optional
SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(16).hex())


for p in (DATA_DIR, RECEIPTS_DIR):
    p.mkdir(parents=True, exist_ok=True)
