from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
# Create your views here.
def adminindex(request):
    return render(request,'adminindex.html')