import httpx
import validators
from datetime import datetime
from database.database import SessionLocal, engine
from database.models import PhishingURL
import os

# Tabloyu oluştur
PhishingURL.metadata.create_all(bind=engine)

# Phishing URL'lerini çek
def fetch_phishing_urls():
    print("start fetching")
    urls = []

    # openphish.com'dan veri çekme
    openphish_url = os.getenv("OPENPHISH_URL")
    openphish_response = httpx.get(openphish_url)
    if openphish_response.status_code == 200:
        openphish_urls = openphish_response.text.splitlines()[:50]  # İlk 50 veriyi al
        fetched_date = datetime.now()  # Verinin çekildiği tarih
        urls.extend([(url, fetched_date, 'openphish.com') for url in openphish_urls])
    else:
        print("Failed to fetch from openphish.com")

    # urlhaus.abuse.ch'den veri çekme
    urlhaus_url = os.getenv("URLHAUS_URL")
    urlhaus_response = httpx.get(urlhaus_url)
    if urlhaus_response.status_code == 200:
        urlhaus_urls = urlhaus_response.text.splitlines()[:50]  # İlk 50 veriyi al
        fetched_date = datetime.now()  # Verinin çekildiği tarih
        urls.extend([(url, fetched_date, 'urlhaus.abuse.ch') for url in urlhaus_urls])
    else:
        print("Failed to fetch from urlhaus.abuse.ch")

    # phishtank.com'dan veri çekme
    phishtank_url = "http://data.phishtank.com/data/online-valid.json"
    phishtank_response = httpx.get(phishtank_url)
    if phishtank_response.status_code == 200:
        phishtank_data = phishtank_response.json()
        phishtank_urls = [entry["url"] for entry in phishtank_data[:50]]  # İlk 50 veriyi al
        fetched_date = datetime.now()  # Verinin çekildiği tarih
        urls.extend([(url, fetched_date, 'phishtank.com') for url in phishtank_urls])
    else:
        print("Failed to fetch from phishtank.com")

    # Tekrar eden URL'leri kontrol et ve verilerin URL olduğundan emin ol
    unique_urls = []
    for url_data in urls:
        if url_data[0] not in unique_urls and validators.url(url_data[0]):
            unique_urls.append(url_data)
        else:
            print("Bu veri zaten listede mevcut: ", url_data)

    print("finish fetching")
    return unique_urls


# Çekilen URL'leri veritabanına kaydet
def save_phishing_urls():
    phishing_urls = fetch_phishing_urls()
    SessionLocal.configure(bind=engine)
    session = SessionLocal()
    print("start saving to db")
    for url, fetched_date, source in phishing_urls:
        phishing_url = PhishingURL(url=url, fetched_date=fetched_date, source=source)
        if session.query(PhishingURL).filter(PhishingURL.url == url).first():
            continue
        session.add(phishing_url)
    session.commit()
    session.close()
    print("finish saving to db")


if __name__ == "__main__":
    save_phishing_urls()
