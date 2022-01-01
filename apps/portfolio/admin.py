from django.contrib import admin

from .models import Project, Portfolio, Service
from ..shared.admin import BaseEntityModelAdmin, BaseEntityInline


@admin.register(Service)
class ServiceAdmin(BaseEntityModelAdmin):
    pass


class ProjectAdmin(BaseEntityInline):
    model = Project


@admin.register(Portfolio)
class PortfolioAdmin(BaseEntityModelAdmin):
    inlines = [ProjectAdmin]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.created_by = request.user
            instance.save()
        formset.save_m2m()
