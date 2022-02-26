import imp
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    my_todo = Tenants.objects.all()
    return render(request,'homepage.html',{'my_todo':my_todo})


