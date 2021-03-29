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
import time
#from rpi_ws281x import *
import argparse

Y = " "
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def updatergb(request):
    global Y
    if Y != " ":
        Y.terminate()
    y = Colour.objects.get(name='LED_Strip study table')
    r = request.GET['r']
    g = request.GET['g']
    b = request.GET['b']
    y.red = r
    y.blue = b
    y.green = g
    y.save()
    Y = Process(target=colorWipe(strip, Colour(r, g, b)))
    Y.start()
    data = serialize("json", [y])
    return HttpResponse(data, content_type="application/json")


def updatepower(request):
    global Y
    if Y != " ":
        Y.terminate()
    y = Colour.objects.get(name='LED_Strip study table')
    p = request.GET['p']
    y.power = p
    y.save()
    if p:
        Y = Process(target=colorWipe(strip, Colour(y.red, y.green, y.blue)))
    else:
        Y = Process(target=colorWipe(strip, Colour(0, 0, 0)))
    Y.start()
    data = serialize("json", [y])
    return HttpResponse(data, content_type="application/json")


def senddata(request):
    y = Colour.objects.get(name='LED_Strip study table')
    data = serialize("json", [y])
    return HttpResponse(data, content_type="application/json")


def senddaa(request):
    global Y
    if Y != " ":
        Y.terminate()
    P = Process(target=sendhello)
    Y = P
    P.start()
    return HttpResponse("Working1")

