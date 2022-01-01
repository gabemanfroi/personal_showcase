from rest_framework import viewsets

from apps.website.models import WebsiteContent
from .serializers import WebsiteContentSerializer


class WebsiteContentViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        personal_url = self.kwargs['personal_url']
        queryset = WebsiteContent.objects.filter(personal_url=personal_url)
        return queryset

    queryset = WebsiteContent.objects.all()
    serializer_class = WebsiteContentSerializer

