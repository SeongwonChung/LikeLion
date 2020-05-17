from django.shortcuts import render, redirect
from .models import Article
import time

# Create your views here.
def index_defined_in_view(request):
    articles=Article.objects.all()
    articles_cnt = articles.count()
    movie_cnt = Article.objects.filter(category = 'movie').count()
    drama_cnt = Article.objects.filter(category = 'drama').count()
    entertain_cnt = Article.objects.filter(category = 'entertain').count()

    return render(request, 'index.html', {'articles' : articles, 'articles_cnt' : articles_cnt, 'movie_cnt' : movie_cnt, 'drama_cnt' : drama_cnt, 'entertain_cnt' : entertain_cnt,})

def detail_defined_in_view(request, pk_clicked):
    article = Article.objects.get(pk=pk_clicked)
    
    return render(request, 'detail.html', {'article' : article, })

def new_defined_in_view(request):
    if request.method =='POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            time = time.strftime('%c', time.localtime(time.time()))
        )
        return redirect('detail_i_will_use_in_html', pk_clicked=new_article.pk)
    else: 
        return render(request, 'new.html')

def movie_defined_in_view(request):
    movie_articles = Article.objects.filter(category = 'movie')

    return render(request, 'movie.html', {'movie_articles' : movie_articles,})

def drama_defined_in_view(request):
    drama_articles = Article.objects.filter(category = 'drama')

    return render(request, 'drama.html', {'drama_articles' : drama_articles,})

def entertain_defined_in_view(request):
    entertain_articles = Article.objects.filter(category = 'entertain')

    return render(request, 'entertain.html', {'entertain_articles' : entertain_articles,})