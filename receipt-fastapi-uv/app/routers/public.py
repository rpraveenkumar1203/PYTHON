from __future__ import annotations
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from ..models import ReceiptCreate
from ..services.storage import next_entry_id, append_row
from ..services.pdfgen import build_receipt_pdf
from ..config import RECEIPTS_DIR

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/create", response_class=HTMLResponse)
async def create(
    request: Request,
    name: str = Form(...),
    amount: float = Form(...),
    currency: str = Form("INR"),
):
    payload = ReceiptCreate(name=name.strip(), amount=amount, currency=currency.upper())

    # build entry
    eid = next_entry_id()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        "EntryID": eid,
        "Name": payload.name,
        "Amount": round(payload.amount, 2),
        "Currency": payload.currency,
        "CreatedAt": created_at,
        "ReceiptFilename": f"{eid}.pdf",
    }

    # persist
    append_row(entry)
    pdf_bytes = build_receipt_pdf(entry)
    (RECEIPTS_DIR / entry["ReceiptFilename"]).write_bytes(pdf_bytes)

    return templates.TemplateResponse(
        "success.html", {"request": request, "entry": entry}
    )
