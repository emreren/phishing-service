import httpx
import validators
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # .env dosyasını yükleyin

def fetch_phishing_urls():
    print("start fetching")
    urls = []

    # .env dosyasındaki URL dizesini alın ve virgüllerle bölün
    fetch_urls = os.getenv("URLS").split(',')

    for url in fetch_urls:
        response = httpx.get(url)
        if response.status_code == 200:
            fetched_date = datetime.now()  # Verinin çekildiği tarih
            # Tüm verileri alıp direkt olarak urls listesine ekleyin
            urls.extend([(fetched_url, fetched_date, url) for fetched_url in response.text.splitlines()])
        else:
            print(f"Failed to fetch from {url}")

    # Tekrar eden URL'leri kontrol et ve verilerin URL olduğundan emin ol
    unique_urls = []
    for url_data in urls:
        if url_data[0] not in unique_urls and validators.url(url_data[0]):
            unique_urls.append(url_data)
        else:
            print("Bu veri zaten listede mevcut veya geçersiz URL: ", url_data)

    print("finish fetching")
    return unique_urls
