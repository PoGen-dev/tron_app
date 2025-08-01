from datetime import datetime
from pydantic import BaseModel, Field
from typing import List

class WalletRequest(BaseModel):
    address: str = Field(..., description="Tron wallet address")

class WalletInfo(BaseModel):
    address: str
    balance_trx: float
    bandwidth_used: int
    bandwidth_limit: int
    energy_used: int
    energy_limit: int

class RequestLogOut(BaseModel):
    id: int
    wallet_address: str
    created_at: datetime

    class Config:
        orm_mode = True

class PaginatedLogs(BaseModel):
    total: int
    items: List[RequestLogOut]
