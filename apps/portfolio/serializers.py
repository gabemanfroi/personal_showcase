from rest_framework import serializers

from apps.portfolio.models import Portfolio, Project, Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = Project
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Portfolio
        fields = '__all__'
