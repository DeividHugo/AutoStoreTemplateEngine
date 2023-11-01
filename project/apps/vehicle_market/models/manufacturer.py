from apps.vehicle_market.models.base import BaseModel
from django.db import models


class Manufacturer(BaseModel):
    name = models.CharField(max_length=255, blank=False)

    class Meta:
        db_table = 'manufacturer'
