from django.contrib import admin

from .models import Language, ProgrammingLanguage, SoftSkill, TechSkill, Resume, CustomSkillCategorySkill, \
    CustomSkillCategory, WorkExperience, EducationHistoryItem
# Register your models here.
from ..shared.admin import BaseEntityInline, BaseEntityModelAdmin


class LanguageInline(BaseEntityInline):
    model = Language


class TechSkillInline(BaseEntityInline):
    model = TechSkill


class SoftSkillsInline(BaseEntityInline):
    model = SoftSkill


class ProgrammingLanguageInline(BaseEntityInline):
    model = ProgrammingLanguage


class WorkExperienceInline(BaseEntityInline):
    model = WorkExperience


class EducationHistoryItemInline(BaseEntityInline):
    model = EducationHistoryItem


class CustomSkillCategorySkillInline(BaseEntityInline):
    model = CustomSkillCategorySkill


class CustomSkillCategoryInline(BaseEntityInline):
    model = CustomSkillCategory

    exclude = ['created_by']
    verbose_name = 'Categoria de Habilidades Personalizada (Adicione Habilidades Utilizando o Menu Ao lado)'
    verbose_name_plural = 'Categorias de Habilidades Personalizadas (Adicione Habilidades Utilizando o Menu Ao lado)'


@admin.register(CustomSkillCategory)
class CustomSkillCategoryAdmin(BaseEntityModelAdmin):
    model = CustomSkillCategory
    inlines = [CustomSkillCategorySkillInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.created_by = request.user
            instance.save()
        formset.save_m2m()


@admin.register(Resume)
class ResumeAdmin(BaseEntityModelAdmin):
    inlines = [
        CustomSkillCategoryInline,
        EducationHistoryItemInline,
        LanguageInline,
        ProgrammingLanguageInline,
        SoftSkillsInline,
        TechSkillInline,
        WorkExperienceInline
    ]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.created_by = request.user
            instance.save()
        formset.save_m2m()
