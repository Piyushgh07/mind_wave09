from sqlmodel import SQLModel, Field, Session, create_engine
from typing import Optional
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DATABASE_URL", "sqlite:///./mindwave.db")
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

class Journal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str = Field()
    emotion: str = Field()
    confidence: float = Field()
    forecast: str = Field()
    stress_level: float = Field(default=0.0)   # 🧠 NEW
    crisis_flag: bool = Field(default=False)   # 🚨 NEW
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class Feedback(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    emotion: str = Field()
    tip: str = Field()
    helpful: bool = Field()
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)
