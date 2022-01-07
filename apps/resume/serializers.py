from rest_framework import serializers

from .models import Skill, Language, ProgrammingLanguage, TechSkill, SoftSkill, Resume, CustomSkillCategorySkill, \
    CustomSkillCategory


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        abstract = True
        fields = ['name', 'proficiency']


class LanguageSerializer(SkillSerializer):
    class Meta:
        model = Language
        fields = ['name', 'proficiency']


class ProgrammingLanguageSerializer(SkillSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = ['name', 'proficiency']


class TechSkillSerializer(SkillSerializer):
    class Meta:
        model = TechSkill
        fields = ['name', 'proficiency']


class SoftSkillSerializer(SkillSerializer):
    class Meta:
        model = SoftSkill
        fields = ['name', 'proficiency']


class CustomSkillCategorySkillSerializer(SkillSerializer):
    class Meta:
        model = CustomSkillCategorySkill
        fields = ['name', 'proficiency']


class CustomSkillCategorySerializer(serializers.ModelSerializer):
    custom_skill_category_skills = CustomSkillCategorySkillSerializer(many=True)

    class Meta:
        model = CustomSkillCategory
        fields = ['name', 'custom_skill_category_skills', 'style', 'use_on_resume']


class ResumeSerializer(serializers.ModelSerializer):
    programming_languages = ProgrammingLanguageSerializer(many=True, required=False)
    tech_skills = TechSkillSerializer(many=True, required=False)
    soft_skills = SoftSkillSerializer(many=True, required=False)
    languages = LanguageSerializer(many=True, required=False)
    custom_skill_categories = CustomSkillCategorySerializer(many=True, required=False)

    class Meta:
        model = Resume
        fields = ['programming_languages', 'tech_skills', 'soft_skills', 'languages', 'custom_skill_categories']
