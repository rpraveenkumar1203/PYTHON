from __future__ import annotations
from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from ..services.storage import read_all_rows
from ..config import ADMIN_PASSWORD, XLSX_PATH, RECEIPTS_DIR

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def admin_get(request: Request):
    if ADMIN_PASSWORD:  # gated
        return templates.TemplateResponse(
            "admin.html", {"request": request, "protected": True, "rows": []}
        )
    rows = read_all_rows()
    return templates.TemplateResponse(
        "admin.html", {"request": request, "protected": False, "rows": rows}
    )


@router.post("/", response_class=HTMLResponse)
async def admin_post(request: Request, password: str = Form("")):
    if ADMIN_PASSWORD and password != ADMIN_PASSWORD:
        return templates.TemplateResponse(
            "admin.html",
            {
                "request": request,
                "protected": True,
                "rows": [],
                "error": "Wrong password",
            },
        )
    rows = read_all_rows()
    return templates.TemplateResponse(
        "admin.html", {"request": request, "protected": False, "rows": rows}
    )


@router.get("/export.xlsx")
async def export_excel():
    if not XLSX_PATH.exists():
        raise HTTPException(status_code=404, detail="No data yet")
    return FileResponse(XLSX_PATH, filename="data.xlsx")


@router.get("/receipt/{entry_id}")
async def get_receipt(entry_id: str):
    path = RECEIPTS_DIR / f"{entry_id}.pdf"
    if not path.exists():
        raise HTTPException(status_code=404, detail="Not found")
    return FileResponse(path, filename=f"{entry_id}.pdf")
