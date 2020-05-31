from django.contrib import admin
from .models import Todolist, Comment

# Register your models here.
admin.site.register(Todolist)
admin.site.register(Comment)