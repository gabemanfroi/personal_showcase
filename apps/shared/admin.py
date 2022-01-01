from django.contrib import admin

from .models import PersonalShowcaseUser, Website, UserAdditionalInformation


class BaseEntityModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(BaseEntityModelAdmin, self).get_queryset(request)
        return qs.filter(created_by=request.user)

    def get_changeform_initial_data(self, request):
        return {'created_by': request.user}

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super(BaseEntityModelAdmin, self).save_model(request, obj, form, change)

    readonly_fields = ['created_by']

    class Meta:
        abstract = True


class BaseEntityInline(admin.StackedInline):
    def get_queryset(self, request):
        qs = super(BaseEntityInline, self).get_queryset(request)
        return qs.filter(created_by=request.user)

    classes = ['collapse']

    def get_changeform_initial_data(self, request):
        return {'created_by': request.user}

    readonly_fields = ['created_by']

    extra = 0

    class Meta:
        abstract = True


class WebsiteInline(BaseEntityInline):
    model = Website
    pass


class UserAdditionalInformationInline(BaseEntityInline):
    model = UserAdditionalInformation


@admin.register(PersonalShowcaseUser)
class PersonalShowcaseUser(admin.ModelAdmin):
    inlines = [WebsiteInline, UserAdditionalInformationInline]
