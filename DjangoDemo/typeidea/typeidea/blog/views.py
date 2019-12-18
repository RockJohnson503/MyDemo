from django.shortcuts import render, get_object_or_404

from .models import Post, Tag, Category


def post_list(request, category_id=None, tag_id=None):
    tag, category = None, None
    post_list = Post.objects.filter(status=Post.STATUS_NORMAL)

    if tag_id:
        tag = get_object_or_404(Tag, pk=tag_id)
        post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    elif category_id:
        category = get_object_or_404(Category, pk=category_id)
        post_list = post_list.filter(category_id=category_id)

    context = {
        'tag': tag,
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/list.html', context=context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})
