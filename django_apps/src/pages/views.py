from django.shortcuts import render
# pages/views.py
from django.http import HttpResponse


def homePageView(request): # returns the website home page
    return HttpResponse("Hello, World!")