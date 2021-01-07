from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Event (models.Model):
    EventName = models.CharField(max_length = 32)
    Desc = models.TextField(blank = True, max_length = 50)
    Loc = models.CharField(max_length = 32)
    FromDate = models.DateField(default = datetime.date.today)
    FromTime = models.TimeField(default = timezone.now)
    ToDate = models.DateField(default = datetime.date.today)
    ToTime = models.TimeField(default = timezone.now)
    RegEndDate = models.DateField(default = datetime.date.today)
    RegEndTime = models.TimeField(default = timezone.now)
    HostEmail = models.EmailField(max_length = 254)
    HostPassword = models.CharField(max_length = 32)
    Status = models.IntegerField()

    def __str__ (self):
        return self.EventName
