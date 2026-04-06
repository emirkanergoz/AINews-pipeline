import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

url = "https://webrazzi.com/"

# User-Agent'ı biraz daha güncelleyelim
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

def scrape_news():
    try:
        response = requests.get("https://webrazzi.com/", headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            raw_titles = soup.find_all(["h2", "h3"])
        
            news_data = []

            for item in raw_titles:
                title_text = item.get_text(strip=True)

                if len(title_text) > 20:
                    news_entry = {
                        "title": title_text,
                        "source": "Webrazzi",
                        "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                news_data.append(news_entry)

            with open("webrazzi_news.json", "w", encoding="utf-8") as f:
                json.dump(news_data, f, ensure_ascii=False, indent=4)

            print(f"Succes! {len(news_data)} news items scraped and saved to webrazzi_news.json")
              
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    
    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    scrape_news()

                