# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from .models import Sightings


# Create your views here.
def index(request):
    sighting_list = Sightings.objects.order_by('date_posted')[:5]
    context = {
        'sighting_list': sighting_list,
    }
    return render(request, 'freeApp/index.html', context)

def detail(request, sighting_id):
    sighting = Sightings.objects.get(pk=sighting_id)
    context = {
        'sighting': sighting
    }
    return render(request, 'freeApp/detail.html', context)