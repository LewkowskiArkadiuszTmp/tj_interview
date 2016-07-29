from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# todo
def index(request):
    data = {}
    data['html'] = ''
    data['title'] = ''
    data['description'] = ''
    return JsonResponse(data)
