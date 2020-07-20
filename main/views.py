from django.shortcuts import render
from login.models import Account

def main(request):
    return render(request, 'main.html')

def notyet(request):
    return render(request, 'notyet.html')
    
# Create your views here.
