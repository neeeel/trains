from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Journey,JourneyStop
from django.template import loader
from .forms import NameForm
import django.contrib.auth.forms


def get_name(request):
    form1 = NameForm()
    return render(request,"trains/name.html",{"form":form1})

def index(request):
    form1= django.contrib.auth.forms.UserCreationForm
    return render(request,"index.html",{"form":form1})

def listJourneys(request):
    journeys = Journey.objects.all()
    for j in journeys:
        print(j.scotrailID)
    #output = ', '.join([p.tracsisID for p in journeys])


    template = loader.get_template("trains/listJourneys.html")
    context = {"latest_journey_list":journeys}
    return render(request, 'trains/listJourneys.html',context=context)


def detail(request, journey_id):
    stops = Journey.objects.get(pk=journey_id).journeystop_set.all()
    #result = []
    #for s in stops:
        #result.append([s.station.name , str(s.depTime)])
    context = {"full_journey":stops}
    return render(request, 'trains/fullJourney.html',context=context)




