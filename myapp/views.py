from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_worls(request):
    return HttpResponse("Hello Wotld") 

def homePage(request):
    return render(request,"index.html")

def taskPage(request):
    return render(request,"task.html")