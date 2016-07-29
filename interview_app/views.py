from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from bs4 import BeautifulSoup
import urllib2

# todo
def index(request, url_parameter):
    try:
        url = url_parameter
    except:
        raise Http404("Not Found")
    data = {}


    data['html'] = ''
    data['title'] = ''
    data['description'] = ''
    return JsonResponse(data)
