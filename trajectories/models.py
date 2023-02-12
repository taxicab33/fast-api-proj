from common_data.mixins import SoftDeleteMixin
from common_data.models import CommonDataMixin, CreatorDataMixin, BaseModel


class Trajectory(BaseModel,
                 CommonDataMixin,
                 SoftDeleteMixin,
                 CreatorDataMixin):
    pass

