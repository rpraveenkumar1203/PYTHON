from __future__ import annotations
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import public, admin
from .config import DATA_DIR, RECEIPTS_DIR
from .services.storage import ensure_workbook

app = FastAPI(title="Receipt Webapp")

# storage bootstrap
ensure_workbook()

# mount receipts as static for direct linking (optional)
app.mount("/receipts", StaticFiles(directory=str(RECEIPTS_DIR)), name="receipts")

# routes
app.include_router(public.router)
app.include_router(admin.router)


# # 1) (Optional) set an admin password
# export ADMIN_PASSWORD="secret123"   # Windows PowerShell: $env:ADMIN_PASSWORD="secret123"

# # 2) Install deps via uv (reads pyproject.toml)
# uv sync

# # 3) Run the dev server
# uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
# # or use the shortcut:
# uv run dev
