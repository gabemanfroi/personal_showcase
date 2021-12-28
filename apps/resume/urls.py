from django.urls import path, include
from rest_framework import routers

from .views import ResumeViewSet

router = routers.SimpleRouter()
router.register(r'', ResumeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
