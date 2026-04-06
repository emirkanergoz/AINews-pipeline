import requests
from bs4 import BeautifulSoup

url = "https://webrazzi.com/"

# User-Agent'ı biraz daha güncelleyelim
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # class_ kısmını sildik, çünkü o bizi kısıtlıyordu. 
        # Sitedeki tüm h2 ve h3 etiketlerini (başlıkları) çekiyoruz.
        titles = soup.find_all(["h2", "h3"])

        print(f"Toplam {len(titles)} adet başlık bulundu.\n")

        for i, baslik in enumerate(titles, 1):
            metin = baslik.get_text(strip=True)
            # Menü linkleri gibi çok kısa metinleri eleyelim, gerçek haberleri görelim
            if len(metin) > 20: 
                print(f"{i}. {metin}")
    else:
        print(f"Bağlantı hatası: {response.status_code}")

except Exception as e:
    print(f"Hata oluştu: {e}")