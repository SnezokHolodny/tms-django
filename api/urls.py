from django.urls import path, include
from rest_framework import routers
from .import views


router = routers.DefaultRouter()
router.register('questions', views.QuestionsViewSet)
router.register('choices', views.ChoiceViewSet)
router.register('articles', views.ArticleViewSet)
router.register('authors', views.AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]