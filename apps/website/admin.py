from django.contrib import admin

from apps.blog.models import Blog
from apps.portfolio.models import Portfolio
from apps.resume.models import Resume
from apps.shared.admin import BaseEntityModelAdmin, BaseEntityInline
from apps.website.models import CarrouselItem, WebsiteContent


class CarrouselItemInline(BaseEntityInline):
    model = CarrouselItem


@admin.register(WebsiteContent)
class WebsiteContentAdmin(BaseEntityModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "resume":
            kwargs["queryset"] = Resume.objects.filter(created_by=request.user)
        if db_field.name == "portfolio":
            kwargs["queryset"] = Portfolio.objects.filter(created_by=request.user)
        if db_field.name == 'blog':
            kwargs["queryset"] = Blog.objects.filter(created_by=request.user)
        return super(WebsiteContentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.created_by = request.user
            instance.save()
        formset.save_m2m()

    inlines = [CarrouselItemInline]
    fields = ['resume', 'portfolio', 'personal_url', 'background_image']
    pass
