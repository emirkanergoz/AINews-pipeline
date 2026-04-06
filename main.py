from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_PATH = os.path.join(BASE_DIR, "templates")
DATA_FILE = os.path.join(BASE_DIR, "news_data.json")

templates = Jinja2Templates(directory=TEMPLATES_PATH)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    if not os.path.exists(DATA_FILE):
        return "<h1>Veri dosyası bulunamadı! Önce scraper.py çalıştır.</h1>"
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    # HATAYI ÇÖZEN KRİTİK DEĞİŞİKLİK:
    # Context sözlüğünü ayrı bir değişkene alıp öyle gönderiyoruz.
    context = {
        "request": request,
        "news_list": data,
        "count": len(data)
    }
    
    return templates.TemplateResponse(request=request, name="index.html", context=context)