from sqlalchemy import create_engine, text
import os

raw_url = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Normalize Heroku-style scheme -> SQLAlchemy dialect
if raw_url.startswith("postgres://"):
    raw_url = raw_url.replace("postgres://", "postgresql+psycopg2://", 1)

engine = create_engine(raw_url, echo=True, future=True)

def init_db():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
