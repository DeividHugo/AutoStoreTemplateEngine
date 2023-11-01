from apps.core.models.base import BaseModel
from django.db import models


class ManufacturerBrand(BaseModel):
    name = models.CharField(max_length=255, blank=False)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)

    class Meta:
        db_table = 'manufacturer_brand'
