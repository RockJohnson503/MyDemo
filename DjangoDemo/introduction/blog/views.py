from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator

from .models import Article

def hello_world(request):
    return HttpResponse("hello world")

def article_content(request):
    page = request.GET.get('page') or 1
    try:
        page = int(page)
    except:
        return HttpResponseNotFound()

    article_main = Article.objects.order_by('-publish_date')
    article_new = article_main[:10]
    paginator = Paginator(article_main, 5)
    page_lst = paginator.page(page)
    next_page = None
    prev_page = None

    if page_lst.has_next():
        next_page = page + 1
    if page_lst.has_previous():
        prev_page = page - 1

    return render(request, 'blog/index.html', {'article_main': page_lst, 'article_new': article_new,
                                               'page_num': range(1, paginator.num_pages + 1),
                                               'curr_page': page, 'next_page': next_page, 'prev_page': prev_page})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    try:
        article_next = article.get_next_by_publish_date()
    except:
        article_next = None
    try:
        article_prev = article.get_previous_by_publish_date()
    except:
        article_prev = None

    return render(request, 'blog/detail.html', {'article': article, 'article_prev': article_prev, 'article_next': article_next})