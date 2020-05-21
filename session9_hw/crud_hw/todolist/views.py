from django.shortcuts import render,redirect
from .models import Todolist
import datetime as dt
import pytz

# Create your views here.
def home(request):
    todolist = Todolist.objects.all().order_by('deadline')
    
    for todo in todolist:
        timeleft = todo.deadline - dt.datetime.now(pytz.utc) - dt.timedelta(hours=9)
        timeleft_f = {"days" : timeleft.days, "hours" : timeleft.seconds//3600,}
        timeleft_str = f"{timeleft_f['days']} 일 {timeleft_f['hours']} 시간"
        todo.timeleft = timeleft_str

    return render(request, 'home.html', {'todolist' : todolist, })

def detail(request, todo_pk):
    todo = Todolist.objects.get(pk = todo_pk)

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