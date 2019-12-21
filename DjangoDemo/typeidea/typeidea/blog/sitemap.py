# encoding: utf-8

"""
File: sitemap.py
Author: Rock Johnson
"""
from django.urls import reverse
from django.contrib.sitemaps import Sitemap

from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'always'
    priority = 1.0
    protocol = 'https'

    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)

    def lastmod(self, obj):
        return obj.created_time

    def location(self, obj):
        return reverse('blog:detail', args=(obj.pk,))
