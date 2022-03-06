from .models import Article
from django.shortcuts import render
import time
from .service.query_processing.HandleQuery import search
from .form import PostForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def articles(request):
    form = PostForm(request.POST or None)
    q = request.POST.get('query')
    start_time = time.time()
    id_articles = search(q)
    if id_articles == -1:
        articles = [" Invalid query!"]
        number_articles = 0
    else :
        articles = Article.objects.filter(id_article__in=id_articles)
        number_articles = len(articles)

    end_time = time.time()
    execute_time = end_time - start_time
    return render(request, 'articles.html', {"articles": articles,"number_articles": number_articles, "execute_time": execute_time, "f": form})

def article_detail_view (request, id):
    article = Article.objects.get(id_article=id)
    return render(request, 'detail.html', {"content" : article.content})