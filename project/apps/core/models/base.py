from django.db import models
from apps.core.models.managers import ActiveObjectsManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = ActiveObjectsManager() 

    class Meta:
        abstract = True

    def delete(self):
        self.is_active = False
        self.save()

    def undelete(self):
        self.is_active = True
        self.save()

    def __str__(self):
        return str(self.pk)
