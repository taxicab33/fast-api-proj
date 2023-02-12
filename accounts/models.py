from sqlalchemy import String, Column, DateTime, Boolean
from common_data.mixins import SoftDeleteMixin
from common_data.models import BaseModel


class User(BaseModel,
           SoftDeleteMixin):
    username = Column(
        String(length=255),
        unique=True,
        index=True
    )
    email = String(
        length=255
    )
    password = Column(
        String
    )
    joined_at = Column(
        DateTime
    )
    is_active = Column(
        Boolean,
        default=False
    )
    is_admin = Column(
        Boolean,
        default=False
    )
    is_staff = Column(
        Boolean,
        default=False
    )

