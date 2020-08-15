from django.shortcuts import render
from django.http import HttpResponse

# Home page.
def home(request):
    
    return render(request, 'index.html')

# Detials page.
def details(request):

    return render(request, 'details.html')
