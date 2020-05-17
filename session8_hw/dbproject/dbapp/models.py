from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    category = models.CharField(max_length = 10)
    time = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.title
