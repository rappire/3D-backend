from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import json, os


DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(DIR, "secret.json")
DB = json.loads(open(FILE).read())
DB_URL = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"


engine = create_engine(DB_URL, encoding="utf-8", pool_recycle=3600)

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
