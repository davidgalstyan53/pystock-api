from typing import Optional

# Assuming that you have an API key loaded in the environment
from app.config import Settings

settings = Settings()


def get_stock_data(query: str) -> Optional[dict]:
    """
    Mock function to fetch basic stock data based on a search query.
    Replace this with an actual API request to a stock data provider.
    """
    # Sample structure, replace with actual API calls
    sample_data = {
        "AAPL": {"ticker": "AAPL", "name": "Apple Inc.", "current_price": 150.0},
        "TSLA": {"ticker": "TSLA", "name": "Tesla Inc.", "current_price": 720.0},
    }
    # Simulate searching in sample data
    return sample_data.get(query.upper())


def get_stock_details(ticker: str) -> Optional[dict]:
    """
    Mock function to fetch detailed stock information.
    Replace this with an actual API request to a stock data provider.
    """
    # Sample structure, replace with actual API calls
    sample_details = {
        "AAPL": {
            "ticker": "AAPL",
            "name": "Apple Inc.",
            "current_price": 150.0,
            "market_cap": 2500000000000,
            "sector": "Technology",
            "PE_ratio": 28.5,
        },
        "TSLA": {
            "ticker": "TSLA",
            "name": "Tesla Inc.",
            "current_price": 720.0,
            "market_cap": 800000000000,
            "sector": "Automobile",
            "PE_ratio": 32.0,
        },
    }
    return sample_details.get(ticker.upper())
