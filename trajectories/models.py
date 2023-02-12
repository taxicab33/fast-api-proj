from common_data.mixins import SoftDeleteMixin
from common_data.models import CommonDataMixin, CreatorDataMixin
from core.db import Base


class Trajectory(Base,
                 CommonDataMixin,
                 SoftDeleteMixin,
                 CreatorDataMixin):
    pass

