from apps.vehicle_market.models.base import BaseModel
from django.db import models


class VehicleItem(BaseModel):
    name = models.CharField(max_length=255, blank=False)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, blank=False)

    class Meta:
        db_table = 'vehicle_item'
