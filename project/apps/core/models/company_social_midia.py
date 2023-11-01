from apps.core.models.base import BaseModel
from django.db import models


class CompanySocialMidia(BaseModel):
    link = models.CharField(max_length=255, blank=True, null=True)
    social_midia = models.ForeignKey('SocialMidia', on_delete=models.CASCADE, blank=False)

    class Meta:
        db_table = 'company_social_midia'
