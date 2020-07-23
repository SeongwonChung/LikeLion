from django.shortcuts import render, redirect
from .models import Post, Comment, Like, Wish
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', { 'posts': posts })

@login_required(login_url='/registration/login')
def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user
        )
        return redirect('detail', new_post.pk)
    return render(request, 'new.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if (request.method == 'POST'):
        Comment.objects.create(
            post = post, 
            content = request.POST['content'],
            author = request.user
        )
        return redirect('detail', post_pk)

    return render(request, 'detail.html', {'post': post})

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
          title = request.POST['title'],
          content = request.POST['content']
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', {'post': post}) 

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html', { 'error' : error })

        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(
            request,
            new_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect('home')

    return render(request, 'registration/signup.html')

def login(request):
    if (request.method == 'POST'):
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', { 'error': error })

        auth.login(
            request,
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect(request.GET.get('next', '/'))

    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

@csrf_exempt
def like(request):
    if request.method == "POST":
        request_body = json.loads(request.body)
        post_pk = request_body['post_pk']

        existing_like = Like.objects.filter(
            post = Post.objects.get(pk = post_pk),
            user = request.user
        )

        #cancel like
        if existing_like.count() > 0:
            existing_like.delete()
        
        #create like
        else:
            Like.objects.create(
                post = Post.objects.get(pk = post_pk),
                user = request.user
            )

        post_likes = Like.objects.filter(
            post = Post.objects.get(pk = post_pk)
        )

        existNow = Like.objects.filter(
            post= Post.objects.get(pk = post_pk),
            user = request.user
        )
        #json 형태로 response에 like_count 전달.
        response = {
            'like_count' : post_likes.count(), 
            'exist' : existNow.count()
        }
        return HttpResponse(json.dumps(response))

@csrf_exempt
def checkLike(request):
    if request.method == "POST":
        request_body = json.loads(request.body)
        post_pk = request_body['post_pk']

        existing_like = Like.objects.filter(
            post = Post.objects.get(pk = post_pk),
            user = request.user
        )

        exist = existing_like.count()

        response = {
            'exist' : exist
        }
        return HttpResponse(json.dumps(response))

@csrf_exempt
def wish(request):
    if request.method == "POST":
        request_body = json.loads(request.body)
        post_pk = request_body['post_pk']

        existing_wish = Wish.objects.filter(
            post = Post.objects.get(pk = post_pk),
            user = request.user
        )

        #cancel wish
        if existing_wish.count() > 0:
            existing_wish.delete()
        
        #create wish
        else:
            Wish.objects.create(
                post = Post.objects.get(pk = post_pk),
                user = request.user
            )

        post_wishes = Wish.objects.filter(
            post = Post.objects.get(pk = post_pk)
        )

        existNow = Wish.objects.filter(
            post= Post.objects.get(pk = post_pk),
            user = request.user
        )
        #json 형태로 response에 wish_count 전달.
        response = {
            'wish_count' : post_wishes.count(), 
            'exist' : existNow.count()
        }
        return HttpResponse(json.dumps(response))

@csrf_exempt
def checkWish(request):
    if request.method == "POST":
        request_body = json.loads(request.body)
        post_pk = request_body['post_pk']

        existing_wish = Wish.objects.filter(
            post = Post.objects.get(pk = post_pk),
            user = request.user
        )

        exist = existing_wish.count()

        response = {
            'exist' : exist
        }
        return HttpResponse(json.dumps(response))

def mypage(request):
    Posts = Post.objects.all()

    Likes = Like.objects.filter(user = request.user)
    Wishes = Wish.objects.filter(user = request.user)
    
    liked = []
    wished = []

    for like in Likes:
        if like.post in Posts:
            liked.append(like.post)
    
    for wish in Wishes:
        if wish.post in Posts:
            wished.append(wish.post)
    print(liked, type(liked[0].title))
    print(wished)
    return render(request, 'mypage.html', {'liked_posts' : liked, 'wished_posts' : wished})


    