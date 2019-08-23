from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import ArticleSerializer
from .models import Article


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})
    
    def get_single_article(self,request , id):
        articles = Article.objects.get(author_id = id)
        serializer = ArticleSerializer(articles, many=False)
        return Response({"articles": serializer.data})
        

    def post(self, request):
        article = request.data.get('article')

        # Create an article from the above data...
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})
    
    def delete(self , request, id):
        articles = Article.objects.get(author_id = id)
        articles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self , request , id):
        articles = Article.objects.get(author_id = id)
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})
    
 