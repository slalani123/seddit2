from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1>"hi this is a test"</h1>')

# Create your views here.
