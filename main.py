from fastapi import FastAPI
import json
import os

app = FastAPI(title="AI News API", version="1.0.0")

DATA_FILE = "webrazzi_news.json"

@app.get ("/")
def home():
    """Welcome endpoint for our NEWS API."""
    return {
        "message": "Welcome to the AI News API!",
        "status": "Running",
        "endpoints": {
            "all_news": "/news",
            "health": "/health"
        }
    }

@app.get("/news")
def get_news():
    """Reads the JSON file and returns all scraped news items."""

    if not os.path.exists(DATA_FILE):
        return {"message": "No news data found. Run the scraper first!"}
    
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return {
        "count": len(data),
        "data": data
    }

@app.get("/health")
def health_check():
    """Simple endpoint to check if the API is alive."""
    return {"status": "Healthy", "timestamp": "Real-time checks enabled"}