from django.urls import path, include
from rest_framework import routers

from apps.blog.views import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'(?P<personal_url>.+)/(?P<article_title>.+)', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls))
]
