from apps.vehicle_market.models.base import BaseModel
from django.db import models


class CompanyBanner(BaseModel):
    image = models.ImageField(upload_to='company_banner/') 

    class Meta:
        db_table = 'company_banner' 
