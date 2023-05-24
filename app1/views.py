from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first_string(request):
    return  HttpResponse("This is my first _string response in app1")

def firstpage(request):
    return render(request,'firstpage.html')
