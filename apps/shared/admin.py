from django.contrib import admin

from .models import Website, PersonalShowcaseUser


# Register your models here.

@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonalShowcaseUser)
class ResumeUserAdmin(admin.ModelAdmin):
    pass
