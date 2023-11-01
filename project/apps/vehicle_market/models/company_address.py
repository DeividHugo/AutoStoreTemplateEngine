from apps.vehicle_market.models.base import BaseModel
from django.db import models


class CompanyAddress(BaseModel):
    cep = models.CharField(max_length=255)

    class Meta:
        db_table = 'company_address'  
