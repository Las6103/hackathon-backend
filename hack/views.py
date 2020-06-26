from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ArticleSerializer
from .models import Article
<<<<<<< HEAD
# import os
=======
import os
>>>>>>> cfeff56eec7a606a317816ffd39c98d1e6cb4b8c


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (permissions.IsAuthenticated,)
