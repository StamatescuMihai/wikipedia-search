from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from .models import Base

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "resources" / "database.db"

engine = create_engine(f'sqlite:///{DATABASE_PATH}')

Session = sessionmaker(engine)

# create all the tables in the database
def init_db():
	Base.metadata.create_all(bind=engine)

# get database session
@contextmanager
def get_db():
	db = Session()
	try:
		yield db
	except Exception:
		db.rollback()
		raise
	finally:
		db.close()
