from django.db import models
from django.contrib import admin



class BaseModel(models.Model):
    """
    auto_now is for repetitive
    auto_now_add is for 1 time only
    """
    date_modified = models.DateField(auto_now=True, blank=True, null=True)
    modified_by = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True, blank=True, null=True)
    active_status = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        abstract = True