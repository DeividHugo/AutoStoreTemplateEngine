from apps.core.models.base import BaseModel
from django.db import models


class VehiclePhoto(BaseModel):
    image = models.ImageField(upload_to='vehicle_photos/') 
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, blank=False)

    class Meta:
        db_table = 'vehicle_photo'
