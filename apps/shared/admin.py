from django.contrib import admin

from .models import Website, PersonalShowcaseUser, UserAdditionalInformation


# Register your models here.
class BaseAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(BaseAdmin, self).get_queryset(request)
        return qs.filter(user=request.user)

    class Meta:
        abstract = True


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(WebsiteAdmin, self).get_queryset(request)
        return qs.filter(personalshowcaseuser=request.user)


@admin.register(PersonalShowcaseUser)
class ResumeUserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserAdditionalInformation)
class UserAdditionalInformationAdmin(admin.ModelAdmin):
    pass
