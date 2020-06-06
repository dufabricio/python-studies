from django.shortcuts import render
from django.http import HttpResponse

def HelloWorldView(request):
    return HttpResponse('Hello, World!')