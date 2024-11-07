from fastapi import APIRouter, HTTPException
from app.services.stock_service import get_stock_data, get_stock_details

router = APIRouter()


@router.get("/search")
async def search_stock(query: str):
    stock_data = get_stock_data(query)
    if stock_data:
        return stock_data
    raise HTTPException(status_code=404, detail="Stock not found")


@router.get("/details/{ticker}")
async def details(ticker: str):
    stock_info = get_stock_details(ticker)
    if stock_info:
        return stock_info
    raise HTTPException(status_code=404, detail="Stock details not found")
