from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Skill, Language, ProgrammingLanguage, TechSkill, SoftSkill, Resume, CustomSkillCategorySkill, \
    CustomSkillCategory, WorkExperience, EducationHistoryItem


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        abstract = True
        fields = ['id', 'name', 'proficiency']


class LanguageSerializer(SkillSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name', 'proficiency']


class ProgrammingLanguageSerializer(SkillSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = ['id', 'name', 'proficiency']


class TechSkillSerializer(SkillSerializer):
    class Meta:
        model = TechSkill
        fields = ['id', 'name', 'proficiency']


class SoftSkillSerializer(SkillSerializer):
    class Meta:
        model = SoftSkill
        fields = ['id', 'name', 'proficiency']


class CustomSkillCategorySkillSerializer(SkillSerializer):
    class Meta:
        model = CustomSkillCategorySkill
        fields = ['id', 'name', 'proficiency']


class CustomSkillCategorySerializer(serializers.ModelSerializer):
    custom_skill_category_skills = CustomSkillCategorySkillSerializer(many=True)

    class Meta:
        model = CustomSkillCategory
        fields = ['id', 'name', 'custom_skill_category_skills', 'style', 'use_on_resume']


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['id', 'role', 'company_name', 'start_date', 'end_date', 'current']


class EducationHistoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationHistoryItem
        fields = ['id', 'institution_name', 'start_date', 'end_date', 'graduation_name']


class ResumeSerializer(serializers.ModelSerializer):
    work_experiences = SerializerMethodField()
    education_history_items = SerializerMethodField()
    programming_languages = ProgrammingLanguageSerializer(many=True, required=False)
    tech_skills = TechSkillSerializer(many=True, required=False)
    soft_skills = SoftSkillSerializer(many=True, required=False)
    languages = LanguageSerializer(many=True, required=False)
    custom_skill_categories = CustomSkillCategorySerializer(many=True, required=False)

    class Meta:
        model = Resume
        fields = [
            'programming_languages',
            'tech_skills',
            'soft_skills',
            'languages',
            'custom_skill_categories',
            'work_experiences',
            'education_history_items'
        ]

    def get_work_experiences(self, instance):
        work_experiences = instance.work_experiences.order_by('-current', '-end_date')
        return WorkExperienceSerializer(work_experiences, many=True).data


    def get_education_history_items(self, instance):
        education_history_items = instance.education_history_items.order_by('-end_date')
        return EducationHistoryItemSerializer(education_history_items, many=True).data

