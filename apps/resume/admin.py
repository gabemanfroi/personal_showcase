from django.contrib import admin

from .models import Language, ProgrammingLanguage, SoftSkill, TechSkill, Resume
# Register your models here.
from ..shared.admin import BaseEntityModelAdmin, BaseEntityInline


class LanguageInline(BaseEntityInline):
    model = Language


class TechSkillInline(BaseEntityInline):
    model = TechSkill


class SoftSkillsInline(BaseEntityInline):
    model = SoftSkill


class ProgrammingLanguageInline(BaseEntityInline):
    model = ProgrammingLanguage


@admin.register(Resume)
class ResumeAdmin(BaseEntityModelAdmin):
    inlines = [LanguageInline, TechSkillInline, SoftSkillsInline, ProgrammingLanguageInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.created_by = request.user
            instance.save()
        formset.save_m2m()
