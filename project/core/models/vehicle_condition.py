from core.models.base import BaseModel
from django.db import models


class VehicleCondition(BaseModel):
    name = models.CharField(max_length=255, blank=False)

    class Meta:
        db_table = 'vehicle_condition'
