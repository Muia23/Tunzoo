from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PigaKura

# Home page.
def home(request):
    current_user = request.user
    posts = Post.get_posts()

    return render(request, 'index.html', {"current_user": current_user, "posts": posts })

# Detials page.
def details(request,id):
    post = Post.get_post_details(id)

    return render(request, 'details.html', {"post" : post})

#Reviewing page.(Kura)
@login_required(login_url='/accounts/login/')
def kura(request,id):
    post = Post.get_post_details(id)
    if request.method == 'POST':
        kuraform  = PigaKura(request.POST, request.FILES)
        if kuraform.is_valid():            
            kura = kuraform.save(commit=False)
            kura.save()            
        return redirect('home')                
    else:
        kuraform = PigaKura()

    return render(request, 'review.html', {"post" : post, "kuraform" : kuraform})