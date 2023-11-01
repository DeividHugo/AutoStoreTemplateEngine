from apps.core.models.base import BaseModel
from django.db import models


class Vehicle(BaseModel):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)
    kms = models.IntegerField(blank=False)
    year = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    seats = models.IntegerField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    vehicle_condition = models.ForeignKey('VehicleCondition', on_delete=models.CASCADE, blank=True, null=True)
    vehicle_classification = models.ForeignKey('VehicleClassification', on_delete=models.CASCADE, blank=True, null=True)
    vehicle_gear = models.ForeignKey('VehicleGear', on_delete=models.CASCADE, blank=True, null=True)
    manufacture_brand_version = models.ForeignKey('ManufactureBrandVersion', on_delete=models.CASCADE, blank=False)

    class Meta:
        db_table = 'vehicle'
