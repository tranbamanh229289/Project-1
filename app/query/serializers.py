from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id_article', 'content')

class RequestSerializer(serializers.Serializer):
    query = serializers.CharField(max_length=100)
