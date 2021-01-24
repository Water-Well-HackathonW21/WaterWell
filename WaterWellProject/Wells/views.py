from django.shortcuts import render
from .models import Well
import json
from django.core import serializers
from .forms import WellMarker

# Create your views here.

def index (request):

    # if request.method == 'POST' and request.is_ajax():
    #     pass
    # else:
    # all_items = Well.objects.all()
    json_serializer = serializers.get_serializer("json")()
    all_items = json_serializer.serialize(Well.objects.all())
    return render (request, 'Wells/main.html', {'all_items': all_items})

def add (request):
    if request.method == 'POST':
        print(request.body)
        res = json.loads(request.body)
        print(res["status"])
        Well(status = res["status"], lat = res["lat"], lon = res["lon"], description = res["description"]).save()
        # WellMarker.objects.create(status = res["status"], lat = res["lat"], lon = res["lon"], description = res["description"])
        json_serializer = serializers.get_serializer("json")()
        all_items = json_serializer.serialize(Well.objects.all())



        return render (request, 'Wells/main.html', {'all_items': all_items})
    #     form = WellMarker(request.POST or None)
    #     print(request.body)

    # if form.is_valid():
    #     form.save()
    #     json_serializer = serializers.get_serializer("json")()
    #     all_items = json_serializer.serialize(Well.objects.all())
        
