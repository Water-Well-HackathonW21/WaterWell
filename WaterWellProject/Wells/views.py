from django.shortcuts import render
from .models import Well
import json
from django.core import serializers

# Create your views here.

def index (request):

    # if request.method == 'POST' and request.is_ajax():
    #     pass
    # else:
    # all_items = Well.objects.all()
    json_serializer = serializers.get_serializer("json")()
    all_items = json_serializer.serialize(Well.objects.all().order_by('id'))
    return render (request, 'Wells/main.html', {'all_items': all_items})