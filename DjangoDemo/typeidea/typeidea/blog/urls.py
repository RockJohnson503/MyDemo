"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from .apis import PostViewSet, CategoryViewSet
from .views import (
    TagView, IndexView, SearchView, AuthorView,
    CategoryView, PostDetailView,
)


router = DefaultRouter()
router.register('post', PostViewSet, basename='api-post')
router.register('category', CategoryViewSet, basename='api-category')
app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag'),
    path('post/<int:pk>.html', PostDetailView.as_view(), name='detail'),
    path('author/<int:owner_id>/', AuthorView.as_view(), name='author'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),

    # api
    path('api/', include(router.urls)),
    path('api/docs/', include_docs_urls(title='typeidea apis')),
]
