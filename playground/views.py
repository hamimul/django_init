from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    # return HttpResponse('Http response sent')
    return render(request,'hello.html',{'Answer':'Yes'})