from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length = 200)
    detail = models.TextField()
    deadline = models.DateTimeField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'todos')
    def __str__(self):
        return self.title

class Comment(models.Model):
    todo = models.ForeignKey(Todolist, on_delete = models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comments')

    class Meta :
        ordering = ('-pk',)