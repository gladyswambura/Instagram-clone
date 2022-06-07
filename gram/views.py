from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse, resolve
from django.contrib import messages
from . forms import *
from django.contrib.auth.decorators import login_required
from .models import Post, Profile, Follow, Stream, Comment
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q


# SEARCH
def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            results = User.objects.filter(Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))
            return render(request, 'main/search.html', {'results': results})
        else:
            return render(request, 'main/search.html')
    else:
        return render(request, 'main/search.html')



# MAIN PAGE VIEW
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.objects.all().order_by('-posted')
    return render(request, 'main/index.html',{'posts':posts})


# NEW POST FUNCTION
@login_required(login_url='/accounts/login/')
def NewPost(request):
    if request.method=='POST':
        picture=request.FILES.get('photo')
        caption=request.POST.get('caption')
        img=Post(picture=picture,caption=caption,user=request.user)
        img.save_picture()
        return redirect('index')
    return render(request,'main/newpost.html')

# POST-DETAILS FUNCTION
@login_required(login_url='/accounts/login/')
def PostDetail(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-date')

    if request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user
            comment.save()
            return HttpResponseRedirect(reverse('post-detail', args=[post.id]))
    else:
        form = NewCommentForm()

    context = {
        'post': post,
        'form': form,
        'comments': comments
    }

    return render(request, 'post_detail.html', context)


# LIKE POST FUNCTION
@login_required(login_url='/accounts/login/')
def like(request,operation,pk):
    post = get_object_or_404(Post,pk=pk)
    
    if operation == 'like':
        post.likes += 1
        post.save()
    elif operation =='unlike':
        post.likes -= 1
        post.save()
    return redirect('index')
    

@login_required(login_url='/accounts/login/')
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = current_user
            comment.save()
            return redirect('index')
    else:
        form = NewCommentForm()
        return render(request, 'main/comment.html', {"user": current_user, "comment_form": form})

# FAVOURITE POST FUNCTION
@login_required(login_url='/accounts/login/')
def favourite(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    profile = Profile.objects.get(user=user)

    if profile.favourite.filter(id=post_id).exists():
        profile.favourite.remove(post)
    else:
        profile.favourite.add(post)
    return HttpResponseRedirect(reverse('post-detail', args=[post_id]))


# **********Profile view starts here******************
# PROFILE FUNCTION
@login_required(login_url='/accounts/login/')
def profile(request):
    userupdate = UpdateUserForm()
    context = {
        'userupdate': userupdate,
    }
    return render(request, 'users/profile.html', context)

# UPDATE PROFILE FUNCTION
@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        updateprofile = UpdateProfileForm(request.POST,request.FILES)
        if updateprofile.is_valid():
            profile = updateprofile.save(commit=False)
            profile.user = current_user
            profile.save()
        
        messages.success(request,'Your Profile account has been updated successfully')
        return redirect('index')
    else:
        updateprofile = NewProfileForm() 
    params = {
        'updateprofile':updateprofile
    }
    return render(request,'users/update_profile.html',params)

# FOLLOW
def follow(request,operation,id):
    current_user=User.objects.get(id=id)
    if operation=='follow':
        Follow.follow(request.user,current_user)
        return redirect('index')
    elif operation=='unfollow':
        Follow.unfollow(request.user,current_user)
        return redirect('index')

# def follow(request, username, option):
#     follower = request.user
#     following = get_object_or_404(User, username=username)

#     try:
#         f, created = Follow.objects.get_or_create(follower=request.user, following=following)

#         if int(option) == 0:
#             f.delete()
#             Stream.objects.filter(following=following, user=request.user).all().delete()

#         return HttpResponseRedirect(reverse('profile', args=[username]))

#     except User.DoesNotExist:
#         return HttpResponseRedirect(reverse('profile', args=[username]))


