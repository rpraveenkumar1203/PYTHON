from __future__ import annotations
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def build_receipt_pdf(entry: dict) -> bytes:
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    W, H = A4

    # header
    c.setFillColorRGB(0.12, 0.12, 0.15)
    c.rect(0, H - 40, W, 40, fill=1, stroke=0)
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(20, H - 28, "Payment Receipt")

    # body
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica", 11)
    y = H - 80
    gap = 18

    def row(label, value):
        nonlocal y
        c.setFont("Helvetica-Bold", 11)
        c.drawString(30, y, f"{label}:")
        c.setFont("Helvetica", 11)
        c.drawString(140, y, str(value))
        y -= gap

    row("Receipt ID", entry["EntryID"])
    row("Name", entry["Name"])
    row("Amount", f"{entry['Amount']} {entry['Currency']}")
    row("Created At", entry["CreatedAt"])

    c.setFont("Helvetica-Oblique", 9)
    c.setFillColorRGB(0.25, 0.25, 0.25)
    c.drawString(30, 30, "This is a system-generated receipt.")

    c.showPage()
    c.save()
    buf.seek(0)
    return buf.getvalue()
