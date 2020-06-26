from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('articles/', views.ArticleList.as_view(), name='article_list'),
    path('articles/<int:pk>', views.ArticleDetail.as_view(), name='article_detail'),
]
