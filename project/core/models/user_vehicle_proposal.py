from core.models.base import BaseModel
from django.db import models


class UserVehicleProposal(BaseModel):
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    message = models.TextField(blank=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=False)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, blank=False)

    class Meta:
        db_table = 'user_vehicle_proposal'
