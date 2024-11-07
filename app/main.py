from fastapi import FastAPI
from app.routes import stocks
from app.config import Settings

settings = Settings()

app = FastAPI(
    title=settings.api_name,
    description="A REST API for searching stocks and retrieving details.",
    version="1.0.0",
)

app.include_router(stocks.router, prefix="/stocks", tags=["Stocks"])


@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.api_name}"}
