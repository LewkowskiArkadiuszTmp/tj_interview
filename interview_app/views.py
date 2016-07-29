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

    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)

    description = soup.findAll(attrs={"name":"description"})
    title = soup.title.string

    data = {}
    data['html'] = ''
    data['title'] = title.encode('utf-8')
    data['description'] = description[0]['content'].encode('utf-8')

    #import pdb; pdb.set_trace()
    return JsonResponse(data)
