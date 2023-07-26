from phishing_service.database.database import SessionLocal
from phishing_service.database.models import PhishingURL
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, Query

app = FastAPI()

# Veritabanı oturumu almak için yardımcı fonksiyon
def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Phishing URL'lerini listeleyen API endpointi
@app.get("/phishing-urls/")
def get_phishing_urls(skip: int = Query(0, ge=0), limit: int = Query(200, le=1000), db: Session = Depends(get_db)):
    # Eğer limit değeri belirtilmediyse, limit değerini 200 olarak ayarla
    urls = db.query(PhishingURL).offset(skip).limit(limit).all()
    return {"phishing_urls": urls}
