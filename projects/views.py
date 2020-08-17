from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

# Home page.
def home(request):
    
    return render(request, 'index.html')

# Detials page.
@login_required(login_url='/accounts/login/')
def details(request):

    return render(request, 'details.html')
