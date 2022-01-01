from rest_framework import serializers

from apps.portfolio.serializers import PortfolioSerializer
from apps.resume.serializers import ResumeSerializer
from apps.shared.serializers import PersonalShowcaseUserSerializer
from apps.website.models import CarrouselItem, WebsiteContent


class CarrouselItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrouselItem
        fields = '__all__'


class WebsiteContentSerializer(serializers.ModelSerializer):
    resume = ResumeSerializer()
    created_by = PersonalShowcaseUserSerializer()
    carrousel_items = CarrouselItemSerializer(many=True)
    portfolio = PortfolioSerializer()

    class Meta:
        model = WebsiteContent
        fields = ['resume', 'portfolio', 'background_image', 'carrousel_items', 'created_by']
