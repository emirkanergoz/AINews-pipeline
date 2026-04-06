import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import logging
import os

# Get the current directory to save files correctly
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(
    filename=os.path.join(BASE_DIR, 'app.log'), 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

TARGET_URL = "https://webrazzi.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

def scrape_news():
    try:
        logging.info("Scraping started...")
        response = requests.get(TARGET_URL, headers=HEADERS)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            raw_titles = soup.find_all(["h2", "h3"])
            
            news_data = []
            seen_titles = set()

            for item in raw_titles:
                title_text = item.get_text(strip=True)
                
                if len(title_text) > 20 and title_text not in seen_titles:
                    news_entry = {
                        "title": title_text,
                        "source": "Webrazzi",
                        "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    news_data.append(news_entry)
                    seen_titles.add(title_text)

            # SAVE AS news_data.json
            output_path = os.path.join(BASE_DIR, "news_data.json")
            with open(output_path, "w", encoding="utf-8") as file:
                json.dump(news_data, file, ensure_ascii=False, indent=4)
            
            print(f"Success! {len(news_data)} news items saved to news_data.json")
            logging.info(f"Saved {len(news_data)} items.")
            
        else:
            logging.error(f"Status code error: {response.status_code}")

    except Exception as error:
        logging.error(f"Scraper error: {error}")

if __name__ == "__main__":
    scrape_news()