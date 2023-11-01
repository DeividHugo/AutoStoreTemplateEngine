from apps.core.models.base import BaseModel
from django.db import models


class Fuel(BaseModel):
    name = models.CharField(max_length=255, blank=False)

    class Meta:
        db_table = 'fuel'
