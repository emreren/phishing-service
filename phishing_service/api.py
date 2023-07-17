from database.database import SessionLocal
from database.models import PhishingURL
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends

app = FastAPI()


def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/phishing-urls/")
def get_phishing_urls(db: Session = Depends(get_db)):
    urls = db.query(PhishingURL).all()
    return {"phishing_urls": urls}
