from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Home page.
def home(request):
    current_user = request.user
    posts = Post.get_posts()

    return render(request, 'index.html', {"current_user": current_user, "posts": posts })

# Detials page.
@login_required(login_url='/accounts/login/')
def details(request,id):
    post = Post.get_post_details(id)

    return render(request, 'details.html', {"post" : post})
