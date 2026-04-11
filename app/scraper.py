import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import News

def scrape_and_save():
    db = SessionLocal()
    try:
        response = requests.get("https://webrazzi.com/", headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find_all("article")

        for item in articles:
            title_tag = item.find(["h2", "h3"])
            link_tag = item.find("a")
            img_tag = item.find("img")

            if title_tag and link_tag:
                title_text = title_tag.get_text(strip=True)
                url = link_tag.get("href")
                img_url = img_tag.get("data-src") or img_tag.get("src") if img_tag else None

                # Veritabanında bu haber var mı kontrol et (Tekilleştirme)
                exists = db.query(News).filter(News.url == url).first()
                if not exists:
                    new_news = News(
                        title=title_text,
                        url=url,
                        image=img_url,
                        source="Webrazzi"
                    )
                    db.add(new_news)
        
        db.commit()
        print("Haberler veritabanına başarıyla kaydedildi!")
    except Exception as e:
        print(f"Scraper hatası: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    scrape_and_save()