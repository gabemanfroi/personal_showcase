from rest_framework.viewsets import ModelViewSet

# Create your views here.
from apps.blog.models import Article
from apps.blog.serializers import ArticleSerializer
from apps.website.models import WebsiteContent


class ArticleViewSet(ModelViewSet):
    def get_queryset(self):
        article_title = self.kwargs['article_title']
        personal_url = self.kwargs['personal_url']
        website_content_queryset = WebsiteContent.objects.filter(personal_url=personal_url)
        user = website_content_queryset[0].created_by
        queryset = Article.objects.filter(title=article_title, created_by=user)
        return queryset

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
