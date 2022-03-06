from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Article

# Create your views here.
class ArticleAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all().values()
        return Response(data= articles, status=status.HTTP_200_OK)

    def post(self, request):
        id_article = ['1', '2']
        articles = Article.objects.filter(id_article__in= id_article).values()
        return Response(data=articles, status=status.HTTP_200_OK)