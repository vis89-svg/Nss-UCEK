from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def faculties(request):
    return render(request,'faculties.html')
def attendance(request):
    return render(request,'attendance.html')