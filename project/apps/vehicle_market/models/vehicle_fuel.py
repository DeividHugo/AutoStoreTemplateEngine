from apps.vehicle_market.models.base import BaseModel
from django.db import models


class VehicleFuel(BaseModel):
    fuel = models.ForeignKey('Fuel', on_delete=models.CASCADE, blank=False)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, blank=False)

    class Meta:
        db_table = 'vehicle_fuel'
