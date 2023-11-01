from core.models.base import BaseModel
from django.db import models


class SocialMidia(BaseModel):
    name = models.CharField(max_length=255, blank=False)
    icon = models.ImageField(upload_to='social_midia_icons/') 

    class Meta:
        db_table = 'social_midia'
