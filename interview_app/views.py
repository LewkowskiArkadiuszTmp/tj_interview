from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from bs4 import BeautifulSoup
import urllib2
import hashlib
import re

# todo


def index(request, url_parameter):
    try:
        url = url_parameter
        url_pattern = 'http?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        if not re.match(url_pattern, url):
            raise Http404("Bad url")
    except:
        raise Http404("Not Found")

    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)

    description = soup.findAll(attrs={"name": "description"})
    title = soup.title.string

    data = {}
    data['html'] = str(soup)

    data['title'] = title.encode('utf-8')
    data['description'] = description[0]['content'].encode(
        'utf-8') if description else "No description given"

    return JsonResponse(data)
