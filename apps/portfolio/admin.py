from django.contrib import admin

from .models import Project, Portfolio
from ..shared.admin import BaseEntityModelAdmin, BaseEntityInline


class ProjectAdmin(BaseEntityInline):
    model = Project


@admin.register(Portfolio)
class PortfolioAdmin(BaseEntityModelAdmin):
    inlines = [ProjectAdmin]
