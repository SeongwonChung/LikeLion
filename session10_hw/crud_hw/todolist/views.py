from django.shortcuts import render,redirect
from .models import Todolist, Comment
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
            content = request.POST['content']
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

def new(request):
    if request.method == "POST":

        new_todo = Todolist.objects.create(
            title = request.POST['title'],
            detail = request.POST['detail'],
            deadline = request.POST['deadline']
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
