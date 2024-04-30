from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from config.environments import parameter_store

db_url = f"mysql+pymysql://{parameter_store['DB_USER']}:{parameter_store['DB_PASSWORD']}@{parameter_store['DB_HOST']}/{parameter_store['DB_NAME']}"

engine = create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()