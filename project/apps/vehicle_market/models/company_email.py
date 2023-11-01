from apps.vehicle_market.models.base import BaseModel
from django.db import models
from django.core.validators import EmailValidator


class CompanyEmail(BaseModel):
    address = models.CharField(max_length=255, unique=True, validators=[EmailValidator()])

    class Meta:
        db_table = 'company_email'