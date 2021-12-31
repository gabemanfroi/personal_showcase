from django.contrib import admin

from apps.website.models import CarrouselItem, WebsiteContent


@admin.register(CarrouselItem)
class CarrouselItemAdmin(admin.ModelAdmin):
    pass


@admin.register(WebsiteContent)
class WebsiteContentAdmin(admin.ModelAdmin):
    pass
