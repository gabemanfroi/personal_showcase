from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.shared.models import BaseEntity, PersonalShowcaseUser


class Skill(BaseEntity):
    name = models.CharField(max_length=50, verbose_name='Nome')
    proficiency = models.IntegerField(verbose_name='Nível de Proficiência',
                                      default=1,
                                      validators=[
                                          MaxValueValidator(10),
                                          MinValueValidator(1)
                                      ])

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'


class Language(Skill):
    def get_repr(self) -> str:
        return 'Idioma ' + self.name + ' criado com sucesso!'

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'


class ProgrammingLanguage(Skill):
    def get_repr(self) -> str:
        return 'Linguagem de Programação ' + self.name + ' criada com sucesso!'

    class Meta:
        verbose_name = 'Linguagem de Programação'
        verbose_name_plural = 'Linguagens de Programação'


class TechSkill(Skill):
    def get_repr(self) -> str:
        return 'Habilidade Técnica ' + self.name + ' criada com sucesso!'

    class Meta:
        verbose_name = 'Habilidade Técnica'
        verbose_name_plural = 'Habilidades Técnicas'


class SoftSkill(Skill):

    def get_repr(self) -> str:
        return 'Habilidade Leve' + self.name + ' criada com sucesso!'

    class Meta:
        verbose_name = 'Habilidade Leve'
        verbose_name_plural = 'Habilidades Leves'


class WorkExperience(BaseEntity):
    role = models.CharField(max_length=100, verbose_name='Cargo')
    company = models.CharField(max_length=100, verbose_name='Empresa')
    start_date = models.DateTimeField(
        null=False, blank=False, verbose_name='Data de Início')
    end_date = models.DateTimeField(
        null=True, blank=True, verbose_name='Data de Encerramento')
    current = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.role + ' - ' + self.company

    def get_repr(self) -> str:
        return 'Experiência ' + self.name + ' criada com sucesso!'

    class Meta:
        verbose_name = 'Experiência'
        verbose_name_plural = 'Experiências'


class RoleActivity(BaseEntity):
    description = models.TextField(verbose_name='Atividade Exercida')
    work_experience = models.ForeignKey(
        WorkExperience, on_delete=models.CASCADE)

    def get_repr(self) -> str:
        return 'Atividade ' + self.description + ' criada com sucesso!'

    class Meta:
        verbose_name = 'Atividade do Cargo'
        verbose_name_plural = 'Atividades do Cargo'


class Resume(BaseEntity):
    soft_skills = models.ManyToManyField(to=SoftSkill)
    tech_skills = models.ManyToManyField(to=TechSkill)
    programming_languages = models.ManyToManyField(to=ProgrammingLanguage)
    languages = models.ManyToManyField(to=Language)
    work_experiences = models.ManyToManyField(to=WorkExperience)
    user = models.ForeignKey(to=PersonalShowcaseUser, on_delete=models.CASCADE, default=None)
