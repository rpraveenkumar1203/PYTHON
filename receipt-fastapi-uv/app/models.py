from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional


class ReceiptCreate(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    amount: float = Field(ge=0)
    currency: str = Field(default="INR", min_length=3, max_length=3)


class ReceiptRow(BaseModel):
    EntryID: str
    Name: str
    Amount: float
    Currency: str
    CreatedAt: str
    ReceiptFilename: str
