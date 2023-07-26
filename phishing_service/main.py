from database.database import SessionLocal, engine
from database.models import PhishingURL
from fetch_txt import fetch_phishing_urls

# Phishing URL'lerini çek ve veritabanına kaydet
def save_phishing_urls():
    # Phishing URL'lerini çek
    phishing_urls = fetch_phishing_urls()
    SessionLocal.configure(bind=engine)
    session = SessionLocal()
    print("start saving to db")
    for url, fetched_date, source in phishing_urls:
        phishing_url = PhishingURL(url=url, fetched_date=fetched_date, source=source)
        # Veritabanında aynı URL'ye sahip kayıt varsa, geç
        if session.query(PhishingURL).filter(PhishingURL.url == url).first():
            continue
        # Yeni URL'yi veritabanına ekle
        session.add(phishing_url)
    session.commit()
    session.close()
    print("finish saving to db")

if __name__ == "__main__":
    save_phishing_urls()
