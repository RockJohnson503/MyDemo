# encoding: utf-8

"""
File: serializers.py
Author: Rock Johnson
"""
from rest_framework import serializers, pagination

from .models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    tag = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    owner = serializers.SlugRelatedField(read_only=True, slug_field='username')
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tag', 'owner', 'created_time']


class PostDetailSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tag', 'owner', 'content_html', 'created_time']


class CategorySerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Category
        fields = ['id', 'name', 'created_time']


class CategoryDetailSerializer(CategorySerializer):
    posts = serializers.SerializerMethodField('paginated_posts')

    def paginated_posts(self, obj):
        posts = obj.post_set.filter(status=Post.STATUS_NORMAL)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(page, many=True, context={'request': self.context['request']})
        return {
            'count': posts.count(),
            'results': serializer.data,
            'previous': paginator.get_previous_link(),
            'next': paginator.get_next_link(),
        }

    class Meta:
        model = Category
        fields = ['id', 'name', 'created_time', 'posts']
