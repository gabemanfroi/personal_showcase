from django.contrib import admin

from .models import Article, Subject


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass
