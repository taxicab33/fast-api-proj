import datetime

from sqlalchemy import Column, Boolean, DateTime


class SoftDeleteMixin:

    deleted = Column(
        Boolean,
        default=False
    )
    deleted_at = Column(
        DateTime
    )

    def delete(self):
        self.deleted = True
        self.deleted_at = datetime.datetime.now()
