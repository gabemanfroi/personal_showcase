from rest_framework import serializers

from .models import PersonalShowcaseUser, Website, UserAdditionalInformation


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'category', 'url']
        model = Website


class UserAdditionalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'description']
        model = UserAdditionalInformation


class PersonalShowcaseUserSerializer(serializers.ModelSerializer):
    websites = WebsiteSerializer(many=True)
    additional_information = UserAdditionalInformationSerializer(many=True)

    class Meta:
        fields = ['websites', 'first_name', 'last_name', 'professional_title', 'additional_information',
                  'profile_picture', 'resume_file']
        model = PersonalShowcaseUser
