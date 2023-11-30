from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def testingview(self):
    return HttpResponse("hi, manual cicd pipeline is done")