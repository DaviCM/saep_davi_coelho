from os import getenv

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    getenv(key="DATABASE_URL"),
    pool_pre_ping=True,
    echo=True
)