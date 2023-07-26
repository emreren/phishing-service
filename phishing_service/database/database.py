from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from dotenv import load_dotenv

load_dotenv()

postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_host = os.getenv("POSTGRES_HOST")
postgres_db = os.getenv("POSTGRES_DB")

# PostgreSQL veritabanına bağlantı oluştur
engine = create_engine(
    f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}/{postgres_db}"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Tabloyu oluştur
from .models import PhishingURL
PhishingURL.metadata.create_all(bind=engine)
