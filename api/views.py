from django.shortcuts import render
from rest_framework import viewsets, filters, pagination
from polls.models import Question, Choice
from articles.models import Author, Article
from .serializers import QuestionSerializer, ChoiceSerializer
from .serializers import AuthorSerializer, ArticleSerializer
from django.db.models import Count

class DefaultPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.prefetch_related('choices')
    serializer_class = QuestionSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'question_text', 'pub_date']
    search_fields = ['id', 'question_text', 'pub_date']
    pagination_class = DefaultPagination

    def get_queryset(self):
        queryset = Question.objects.prefetch_related('choices')
        min_choice_count = self.request.query_params.get('min_choice_count')
        if min_choice_count is not None:
            queryset = queryset \
                .annotate(choice_count=Count('choices')) \
                .filter(choice_count__gte=min_choice_count)
        max_choice_count = self.request.query_params.get('max_choice_count')
        if max_choice_count is not None:
            queryset = queryset \
                .annotate(choice_count=Count('choices')) \
                .filter(choice_count__lte=max_choice_count)
        return queryset


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'choice_text', 'pub_date']
    search_fields = ['id', 'choice_text', 'pub_date']
    pagination_class = DefaultPagination

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.prefetch_related('articles')
    serializer_class = AuthorSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer