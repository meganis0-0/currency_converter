from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3)
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    username: str
    password: str

class CurrencyConvert(BaseModel):
    amount: float = Field(..., gt=0)
    from_currency: str
    to_currency: str

class ExchangeRatesResponse(BaseModel):
    base: str
    rates: dict