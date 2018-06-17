import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Sites(models.Model):

    name = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='site_created_by', null=True, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='site_updated_by', null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)
    class Meta:
        db_table = "sites_sites"

    def __str__(self):
        return self.name

class Value(models.Model):

    site = models.ForeignKey(Sites, related_name='value_site', null=True, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    a_value = models.DecimalField(max_digits = 20, decimal_places = 2, null=True)
    b_value = models.DecimalField(max_digits = 20, decimal_places = 2, null=True)
    created_by = models.ForeignKey(User, related_name='value_created_by', null=True, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='value_updated_by', null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)
    class Meta:
        db_table = "sites_value"
