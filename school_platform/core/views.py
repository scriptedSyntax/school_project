from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def welcome(request):
    return render(request, 'core/welcome.html')
