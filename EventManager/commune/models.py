from django.db import models
import datetime
from django.utils import timezone
import os
from twilio.rest import Client

# Create your models here.

class Participant (models.Model):
    REG_TYPE = (
        ('Individual','Individual'),
        ('Group','Group'),
    )
    Name = models.CharField(max_length=50)
    Contact = models.PositiveIntegerField()
    Email = models.EmailField()
    EventReg = models.CharField(max_length = 50)
    RegType = models.CharField(max_length=32, default='Individual', choices=REG_TYPE)
    Number = models.IntegerField(default = 1)

    def __str__ (self):
        return self.Name

class Event (models.Model):
    EVENT_CATEGORY = (
        ('Seminar','Seminar'),
        ('Workshop','Workshop'),
        ('Festival','Festival'),
        ('Competition','Competition'),
        ('Other','Other'),
    )
    
    EventName = models.CharField(max_length = 50)
    Desc = models.TextField(blank = True, max_length = 50)
    Loc = models.CharField(max_length = 32)
    Category = models.CharField(max_length=32, default='Other', choices=EVENT_CATEGORY)
    FromDate = models.DateField(default = datetime.date.today)
    FromTime = models.TimeField(default = timezone.now)
    ToDate = models.DateField(default = datetime.date.today)
    ToTime = models.TimeField(default = timezone.now)
    RegEndDate = models.DateField(default = datetime.date.today)
    RegEndTime = models.TimeField(default = timezone.now)
    HostEmail = models.EmailField(max_length = 254)
    HostPassword = models.CharField(max_length = 32)
    Poster = models.URLField(max_length = 200,blank=True)
    

    def __str__ (self):
        return self.EventName


