from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Kura, Comment, Profile
from .forms import PigaKura, PostForm, CommentForm

# Home page.
def home(request):
    current_user = request.user
    posts = Post.get_posts()

    return render(request, 'index.html', {"current_user": current_user, "posts": posts })

# Detials page.
@login_required(login_url='/accounts/login/')
def details(request,id):
    current_user = request.user
    post = Post.get_post_details(id)    
    kuras = Kura.get_post_kura(id)    
    avrg = Kura.get_average(id)
    comments = Comment.get_comments(id)
    if request.method == 'POST':
        commentform = CommentForm(request.POST, request.FILES)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.user = current_user
            comment.post = post
            comment.save()
        return redirect('home')
    else:
        commentform = CommentForm()

    return render(request, 'details.html', {"post" : post , "avrg" : avrg , "kuras" : kuras , "current_user": current_user, "commentform":commentform, "comments":comments})


#Post a new project
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            post = postform.save(commit=False)
            post.user = current_user            
            post.save()
        return redirect('home')
    
    else:
        postform = PostForm()
    
    return render(request, 'newpost.html', {"postform": postform, "current_user": current_user})

#Reviewing page.(Kura)
@login_required(login_url='/accounts/login/')
def kura(request,id):
    current_user = request.user
    post = Post.get_post_details(id)
    kuras = Kura.get_post_kura(id)
    if request.method == 'POST':
        kuraform  = PigaKura(request.POST, request.FILES)
        if kuraform.is_valid():            
            kura = kuraform.save(commit=False)
            kura.user = current_user
            kura.post = post
            kura.save()            
        return redirect('home')                
    else:
        kuraform = PigaKura()    

    return render(request, 'review.html', {"post" : post, "kuras" : kuras ,"kuraform" : kuraform, "current_user": current_user})

#User Profile
@login_required(login_url='/account/login/')
def profile(request, id):
    current_user = request.user
    profile =Profile.get_profile(id)

    return render(request, 'profile.html', {"profile":profile, "current_user":current_user})