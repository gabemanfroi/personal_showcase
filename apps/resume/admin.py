from django.contrib import admin

from .models import Language, ProgrammingLanguage, SoftSkill, TechSkill, WorkExperience, RoleActivity, Resume


# Register your models here.


class ResumeBaseEntity(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ResumeBaseEntity, self).get_queryset(request)
        print(request.user.id)

        return qs.filter(user=request.user)

    def get_changeform_initial_data(self, request):
        return {'user': request.user}

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ResumeBaseEntity, self).save_model(request, obj, form, change)

    readonly_fields = ['user']

    class Meta:
        abstract = True


@admin.register(Language)
class LanguageAdmin(ResumeBaseEntity):
    pass


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(ResumeBaseEntity):
    pass


@admin.register(SoftSkill)
class SoftSkillAdmin(ResumeBaseEntity):
    pass


@admin.register(TechSkill)
class TechSkillAdmin(ResumeBaseEntity):
    pass


@admin.register(WorkExperience)
class WorkExperienceAdmin(ResumeBaseEntity):
    pass


@admin.register(RoleActivity)
class RoleActivityAdmin(ResumeBaseEntity):
    pass


@admin.register(Resume)
class ResumeAdmin(ResumeBaseEntity):

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "languages":
            kwargs["queryset"] = Language.objects.filter(user=request.user)
        if db_field.name == "tech_skills":
            kwargs["queryset"] = TechSkill.objects.filter(user=request.user)
        if db_field.name == "soft_skills":
            kwargs["queryset"] = SoftSkill.objects.filter(user=request.user)
        if db_field.name == "programming_languages":
            kwargs["queryset"] = ProgrammingLanguage.objects.filter(user=request.user)
        return super(ResumeAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
