from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

def hello_world(request):
    return HttpResponse("hello world")

def article_content(request):
    article_main = Article.objects.all().order_by('publish_date')[:2]
    article_new = Article.objects.all().order_by('publish_date')[:10]

    return render(request, 'blog/index.html', {'article_main': article_main, 'article_new': article_new})

def article_detail(request, article_id):
    article = Article.objects.filter(pk=article_id)[0]

    return render(request, 'blog/detail.html', {'article': article})