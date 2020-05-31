from django.shortcuts import render,redirect
from .models import Todolist, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

import datetime as dt
import pytz

# Create your views here.
def home(request):
    todolist = Todolist.objects.all().order_by('deadline')
    
    for todo in todolist:
        timeleft = todo.deadline - dt.datetime.now(pytz.utc) - dt.timedelta(hours=9)
        timeleft_f = {"days" : timeleft.days, "hours" : timeleft.seconds//3600, "minutes" : timeleft.seconds%3600//60}
        timeleft_str = f"{timeleft_f['days']} 일 {timeleft_f['hours']} 시간 {timeleft_f['minutes']} 분"
        todo.timeleft = timeleft_str
    # 남은 시간을 계산해서 문자열 형태로 변경 후에 todo에 timeleft 로 저장해서 사용한다.
    return render(request, 'home.html', {'todolist' : todolist, })

def detail(request, todo_pk):
    todo = Todolist.objects.get(pk = todo_pk)

    # 남은 시간을 계산해서 문자열 형태로 변경 후에 todo에 timeleft 로 저장해서 사용한다.
    timeleft = todo.deadline - dt.datetime.now(pytz.utc) - dt.timedelta(hours=9)
    timeleft_f = {"days" : timeleft.days, "hours" : timeleft.seconds//3600, "minutes" : timeleft.seconds%3600//60}
    timeleft_str = f"{timeleft_f['days']} 일 {timeleft_f['hours']} 시간 {timeleft_f['minutes']} 분"
    todo.timeleft = timeleft_str

    if request.method == "POST":
        Comment.objects.create(
            todo = todo,
            content = request.POST['content'],
            author = request.user
        )
        return redirect('detail' , todo_pk)


    return render(request, 'detail.html', {'todo' : todo})

def edit(request, todo_pk):
    todo = Todolist.objects.get(pk = todo_pk)
    print(request.POST)
    if request.method == "POST":
        Todolist.objects.filter(pk = todo_pk).update(
            title = request.POST['title'],
            detail = request.POST['detail'],
            deadline = request.POST['deadline']
        )
        return redirect('detail', todo_pk)

    return render(request, 'edit.html', {'todo' : todo})

@login_required(login_url = 'registration/login')
def new(request):
    if request.method == "POST":

        new_todo = Todolist.objects.create(
            title = request.POST['title'],
            detail = request.POST['detail'],
            deadline = request.POST['deadline'],
            author = request.user
        )
        return redirect('detail', new_todo.pk)
    return render(request, 'new.html')

def delete(request, todo_pk):
    todo = Todolist.objects.get(pk = todo_pk)
    todo.delete()

    return redirect('home')

def delete_comment(request, todo_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect( 'detail', todo_pk)

def edit_comment(request, todo_pk, comment_pk):
    todo = Todolist.objects.get(pk = todo_pk)

     # 남은 시간을 계산해서 문자열 형태로 변경 후에 todo에 timeleft 로 저장해서 사용한다.
    timeleft = todo.deadline - dt.datetime.now(pytz.utc) - dt.timedelta(hours=9)
    timeleft_f = {"days" : timeleft.days, "hours" : timeleft.seconds//3600, "minutes" : timeleft.seconds%3600//60}
    timeleft_str = f"{timeleft_f['days']} 일 {timeleft_f['hours']} 시간 {timeleft_f['minutes']} 분"
    todo.timeleft = timeleft_str

    #edit comment
    comment_to_edit = Comment.objects.get(pk = comment_pk)
    if request.method == "POST":
        Comment.objects.filter(pk = comment_pk).update (
            todo = todo_pk,
            content = request.POST['content'],
            author = request.user
        )
        return redirect('detail', todo_pk)
    return render(request, 'edit_comment.html', {'todo' : todo, 'comment_to_edit': comment_to_edit})

## 로그인 기능 추가
def signup(request):
    if request.method == "POST":
        found_user = User.objects.filter(username = request.POST['username'])
        if len(found_user) > 0 :
            error = '이미 존재하는 username입니다'
            return render(request, 'registration/signup.html', {'error' : error})

        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(
            request,
            new_user,
            backend = 'django.contrib.auth.backends.ModelBackend')
        return redirect('home')
    
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == "POST":
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if found_user is None:
            error = "아이디 또는 비밀번호가 틀렸습니다"
            return render(request, 'registration/login.html', {'error' : error})

        auth.login(
            request, 
            found_user,
            backend = 'django.contrib.auth.backends.ModelBackend'
            )
        return redirect(request.GET.get('next', '/'))#new 작성을 위한 login 시에는 GET 으로 전달된 next에 전달되는 '/new/'를 전달해주고 아니면 그냥 home으로.
    
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url = 'registration/login')
def home_private(request):
   
    todolist = Todolist.objects.filter(author = request.user).order_by('deadline')
    username = request.user.username
    
    for todo in todolist:
        timeleft = todo.deadline - dt.datetime.now(pytz.utc) - dt.timedelta(hours=9)
        timeleft_f = {"days" : timeleft.days, "hours" : timeleft.seconds//3600, "minutes" : timeleft.seconds%3600//60}
        timeleft_str = f"{timeleft_f['days']} 일 {timeleft_f['hours']} 시간 {timeleft_f['minutes']} 분"
        todo.timeleft = timeleft_str
    # 남은 시간을 계산해서 문자열 형태로 변경 후에 todo에 timeleft 로 저장해서 사용한다.
    return render(request, 'home_private.html', {'todolist' : todolist, 'username' : username })