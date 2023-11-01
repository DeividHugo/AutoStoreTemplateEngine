from apps.vehicle_market.models.base import BaseModel
from django.db import models


class CompanyPhone(BaseModel):
    international_code = models.CharField(max_length=4, blank=True, null=True)
    local_code = models.CharField(max_length=4, blank=True, null=True)
    number = models.CharField(max_length=14, blank=False)
    
    class Meta:
        db_table = 'company_phone' 
