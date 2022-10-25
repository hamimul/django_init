from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is Http Response from Polls app:index")
# Create your views here.
