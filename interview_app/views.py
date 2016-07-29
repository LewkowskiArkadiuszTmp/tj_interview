from django.shortcuts import render
from django.http import HttpResponse


# todo
def index(request):
    return HttpResponse("Dziala")
