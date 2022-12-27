from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def second(request):
    return HttpResponse('<h1><marquee>yuva is a good boy in my pg in banglore</marquee><h1>')
