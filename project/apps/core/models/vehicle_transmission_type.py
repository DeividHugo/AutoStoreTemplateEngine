from django.db import models
from apps.core.models.base import BaseModel


class VehicleTransmissionType(BaseModel):
    name = models.CharField(max_length=255, blank=False)

    class Meta:
        db_table = 'vehicle_transmission_type'  

    def __str__(self):
        return self.name
