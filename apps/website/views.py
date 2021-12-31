from rest_framework import viewsets

from apps.website.models import WebsiteContent
from .serializers import WebsiteContentSerializer


class WebsiteContentViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        username = self.kwargs['username'].split('-')
        queryset = WebsiteContent.objects.filter(user__first_name=username[0].capitalize(),
                                                 user__last_name=username[1].capitalize())
        return queryset

    queryset = WebsiteContent.objects.all()
    serializer_class = WebsiteContentSerializer
