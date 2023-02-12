from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declared_attr

DATABASE_ENGINE = 'postgresql'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = '54rutyb12'
DATABASE_HOST = 'localhost'
DATABASE_NAME = 'fast_api_test_db'

SQLALCHEMY_DATABASE_URL = f"{DATABASE_ENGINE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class BaseModel(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
        unique=True
    )


Base = declarative_base(cls=BaseModel)
