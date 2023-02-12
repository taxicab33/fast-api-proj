from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship, declared_attr

from accounts.models import User
from core.db import Base


class BaseModel(Base):

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


class CommonDataMixin(object):

    name = Column(
        String
    )


class CreatorDataMixin(object):

    creator = Column(
        Integer,
        ForeignKey(f"{User.__tablename__}.id")
    )

    @declared_attr
    def creator_id(cls):
        return relationship(f"{User.__name__}")
