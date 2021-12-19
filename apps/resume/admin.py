from django.contrib import admin

from .models import Language, ProgrammingLanguage, SoftSkill, TechSkill, WorkExperience, RoleActivity, Resume


# Register your models here.
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(SoftSkill)
class SoftSkillAdmin(admin.ModelAdmin):
    pass


@admin.register(TechSkill)
class TechSkillAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(RoleActivity)
class RoleActivityAdmin(admin.ModelAdmin):
    pass


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass
