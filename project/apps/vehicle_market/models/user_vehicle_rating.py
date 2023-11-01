from apps.vehicle_market.models.base import BaseModel
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class UserVehicleRating(BaseModel):
    rating = models.IntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    feedback = models.TextField(blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=False)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, blank=False)

    class Meta:
        db_table = 'user_vehicle_rating'
