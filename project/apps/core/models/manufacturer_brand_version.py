from apps.core.models.base import BaseModel
from django.db import models


class ManufactureBrandVersion(BaseModel):
    name = models.CharField(max_length=255, blank=False)
    manufacturer_brand = models.ForeignKey('ManufacturerBrand', on_delete=models.CASCADE)

    class Meta:
        db_table = 'manufacture_brand_version'
