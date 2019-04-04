from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('tag/<tag_name>', views.article_tag, name='article_tag'),
    path('message/', views.message, name='message'),
    path('search/', views.MySearchView(), name='search_view',),
]
