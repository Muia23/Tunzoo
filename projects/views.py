from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

# Home page.
def home(request):
    current_user = request.user
    return render(request, 'index.html', {'current_user': current_user })

# Detials page.
@login_required(login_url='/accounts/login/')
def details(request):

    return render(request, 'details.html')
