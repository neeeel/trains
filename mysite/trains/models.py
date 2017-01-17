from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Journey(models.Model):
    scotrailID = models.CharField(max_length=10)
    tracsisID = models.CharField(max_length=10)
    surveyDate = models.DateField()
    scannedDate = models.DateField()
    keyedDate = models.DateField()
    checkedDate =  models.DateField()
    convertedDate =  models.DateField()
    surveyed = models.BooleanField()
    scanned = models.BooleanField()
    keyed = models.BooleanField()
    checked = models.BooleanField()
    converted = models.BooleanField()

    def __str__(self):
        return self.scotrailID


class JourneyStop(models.Model):
    station = models.ForeignKey(Station)
    stopType = models.CharField(max_length=1)  ### o,m,d origin , mid, or destination
    journey = models.ForeignKey(Journey)
    arrTime = models.TimeField()
    depTime = models.TimeField()
    actualArrTime = models.TimeField()
    actualDepTime = models.TimeField()

    def __str__(self):
        return self.station.name + " " + str(self.arrTime)



