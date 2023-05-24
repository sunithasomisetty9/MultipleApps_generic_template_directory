from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2_string(request):
    return HttpResponse("This is my first app2 string response")

def secondpage(request):
    return render(request,'secondpage.html')
