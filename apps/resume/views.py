from rest_framework import viewsets

from apps.resume.models import Resume
from apps.resume.serializers import ResumeSerializer


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
