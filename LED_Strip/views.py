from django.shortcuts import render
from .models import Colour
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework import permissions
from django.core.serializers import serialize
from .LED_paterns import *
from multiprocessing import Process
import threading

P = ""

def updatergb(request):
    y = Colour.objects.get(name='LED_Strip study table')
    r = request.GET['r']
    g = request.GET['g']
    b = request.GET['b']
    y.red = r
    y.blue = b
    y.green = g
    y.save()
    data = serialize("json", [y])
    return HttpResponse(data, content_type="application/json")


def updatepower(request):
    y = Colour.objects.get(name='LED_Strip study table')
    p = request.GET['p']
    y.power = p
    y.save()
    data = serialize("json", [y])
    return HttpResponse(data, content_type="application/json")


def senddata(request):
    y = Colour.objects.get(name='LED_Strip study table')
    data = serialize("json", [y])
    return HttpResponse(data, content_type="application/json")


def senddaa(request):
    P = Process(target=sendhello)
    P.start()
    return HttpResponse("Working1")

