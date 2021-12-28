from rest_framework import serializers

from .models import PersonalShowcaseUser, Website


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['category', 'url']
        model = Website


class PersonalShowcaseUserSerializer(serializers.ModelSerializer):
    websites = WebsiteSerializer(many=True)

    class Meta:
        fields = ['websites', 'first_name', 'last_name']
        model = PersonalShowcaseUser
