from django.contrib import admin

from .models import Project, Portfolio, Service


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass
