from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from apps.core.models.base import BaseModel 


class User(AbstractUser, BaseModel):

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
