from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

watchlist: List[str] = []


@router.get("/")
async def get_watchlist() -> List[str]:
    return watchlist


@router.post("/{ticker}")
async def add_to_watchlist(ticker: str):
    if ticker not in watchlist:
        watchlist.append(ticker)
        return {"message": f"{ticker} added to watchlist"}
    raise HTTPException(status_code=400, detail="Ticker already in watchlist")


@router.delete("/{ticker}")
async def remove_from_watchlist(ticker: str):
    if ticker in watchlist:
        watchlist.remove(ticker)
        return {"message": f"{ticker} removed from watchlist"}
    raise HTTPException(status_code=404, detail="Ticker not found in watchlist")
