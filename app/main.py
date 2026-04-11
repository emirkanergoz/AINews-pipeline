import os
import json
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Dizini ayarla
base_dir = os.path.dirname(os.path.realpath(__file__))
template_path = os.path.join(base_dir, "templates")
templates = Jinja2Templates(directory=template_path)

@app.get("/")
async def read_root(request: Request):
    news_list_data = []
    
    # news_data.json ana dizinde (app klasörünün dışında) olduğu için bir üst dizine çıkıyoruz
    parent_dir = os.path.dirname(base_dir)
    json_path = os.path.join(parent_dir, "news_data.json")

    # Dosyayı oku
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                news_list_data = json.load(f)
        except Exception:
            news_list_data = []

    # HTML'DEKİ DEĞİŞKEN İSİMLERİYLE EŞLEŞTİRME:
    # 1. HTML'de {% for news in news_list %} dediğin için key "news_list" olmalı.
    # 2. Badge için "count" değerini de gönderiyoruz.
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={
            "news_list": news_list_data, 
            "count": len(news_list_data)
        }
    )