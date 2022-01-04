from django.contrib import admin

from .models import Article, Subject, Blog
# Register your models here.
from ..shared.admin import BaseEntityModelAdmin, BaseEntityInline


@admin.register(Subject)
class SubjectInline(BaseEntityModelAdmin):
    pass


class ArticleInline(BaseEntityInline):
    model = Article


@admin.register(Blog)
class BlogAdmin(BaseEntityModelAdmin):
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.created_by = request.user
            instance.save()
        formset.save_m2m()

    inlines = [ArticleInline]
