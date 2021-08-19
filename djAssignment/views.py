from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This assignment was given to me by my mentor Neha Jagadeesh.")

