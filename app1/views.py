from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def page1(request):
    return render(request,"sample.html")

def page2(request):
    return render(request,"sample1.html")

