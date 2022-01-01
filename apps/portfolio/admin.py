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
