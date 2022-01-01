from rest_framework import serializers

from .models import Skill, Language, ProgrammingLanguage, TechSkill, SoftSkill, Resume


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


class ResumeSerializer(serializers.ModelSerializer):
    programming_languages = ProgrammingLanguageSerializer(many=True, required=False)
    tech_skills = TechSkillSerializer(many=True, required=False)
    soft_skills = SoftSkillSerializer(many=True, required=False)
    languages = LanguageSerializer(many=True, required=False)

    class Meta:
        model = Resume
        fields = ['programming_languages', 'tech_skills', 'soft_skills', 'languages']
