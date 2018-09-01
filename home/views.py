from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("lll")
def home(request):
    return render(request, 'seddit/index.html')

# Create your views here.
