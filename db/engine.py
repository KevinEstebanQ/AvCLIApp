from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os
load_dotenv()
engine = create_engine(
    url=os.environ.get("DB_URL"),
    echo=True
)

SessionLocal: sessionmaker[Session] = sessionmaker(bind=engine)