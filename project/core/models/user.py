from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models.base import BaseModel 

class User(AbstractUser, BaseModel):
    
    def __str__(self):
        return self.username
