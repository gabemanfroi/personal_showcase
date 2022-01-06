from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from apps.portfolio.models import Portfolio, Project, Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title']


class ProjectSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = Project
        fields = ['title', 'id', 'image', 'url', 'end_date', 'service']


class PortfolioSerializer(serializers.ModelSerializer):
    projects = SerializerMethodField()

    class Meta:
        model = Portfolio
        fields = ['projects']

    def get_projects(self, instance):
        projects = instance.projects.order_by('-end_date')
        return ProjectSerializer(projects, many=True).data
