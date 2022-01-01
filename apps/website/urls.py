from django.urls import path, include
from rest_framework import routers

from .views import WebsiteContentViewSet

router = routers.DefaultRouter()
router.register(r'(?P<personal_url>.+)', WebsiteContentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
