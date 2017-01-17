from django.test import TestCase

from mysite.trains.models import Journey


# Create your tests here.

journeys = Journey.objects.all()
#for j in journeys:
    #print(j.tracsisID)
