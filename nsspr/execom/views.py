from django.shortcuts import render,redirect
from . models import execom

# Create your views here.
def event(request):
     dict_eve={
         'eve':execom.objects.all()
     }
     return render(request,'execom.html',dict_eve)
