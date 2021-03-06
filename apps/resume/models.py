from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.shared.models import BaseEntity, PersonalShowcaseUser


class Resume(BaseEntity):
    def __str__(self) -> str:
        return self.created_by.username + '\'s Resume'

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'


class WorkExperience(BaseEntity):
    role = models.CharField(max_length=100, verbose_name='Cargo')
    company_name = models.CharField(max_length=100, verbose_name='Empresa')
    start_date = models.DateField(
        null=False, blank=False, verbose_name='Data de Início')
    end_date = models.DateField(
        null=True, blank=True, verbose_name='Data de Encerramento')
    current = models.BooleanField(default=False)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, verbose_name='Resume', related_name='work_experiences')

    def __str__(self) -> str:
        return self.role + ' - ' + self.company_name

    def get_repr(self) -> str:
        return 'Experiência ' + self.name + ' criada com sucesso!'

    class Meta:
        verbose_name = 'Experiência'
        verbose_name_plural = 'Experiências'


class EducationHistoryItem(BaseEntity):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, verbose_name='Resume',
                               related_name='education_history_items')
    institution_name = models.CharField(max_length=100, verbose_name='Instituição')
    start_date = models.DateField(
        null=False, blank=False, verbose_name='Data de Início')
    end_date = models.DateField(
        null=True, blank=True, verbose_name='Data de Encerramento')
    graduation_name = models.CharField(max_length=75, verbose_name='Nome do Curso')
    observation = models.CharField(max_length=100, verbose_name='Observações')

    class Meta:
        verbose_name = 'Item do Histórico Educacional'
        verbose_name_plural = 'Itens do Histórico Educacional'


class RoleActivity(BaseEntity):
    description = models.TextField(verbose_name='Atividade Exercida')
    work_experience = models.ForeignKey(
        WorkExperience, on_delete=models.CASCADE)

    def get_repr(self) -> str:
        return 'Atividade ' + self.description + ' criada com sucesso!'

    class Meta:
        verbose_name = 'Atividade do Cargo'
        verbose_name_plural = 'Atividades do Cargo'


class Skill(BaseEntity):
    name = models.CharField(max_length=50, verbose_name='Nome')
    proficiency = models.IntegerField(verbose_name='Nível de Proficiência',
                                      default=1,
                                      validators=[
                                          MaxValueValidator(100),
                                          MinValueValidator(1)
                                      ])

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'


class Language(Skill):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, verbose_name='Resume', related_name='languages')

    def get_repr(self) -> str:
        return 'Idioma ' + self.name + ' criado com sucesso!'

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'


class ProgrammingLanguage(Skill):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, verbose_name='Resume',
                               related_name='programming_languages')

    def get_repr(self) -> str:
        return 'Linguagem de Programação ' + self.name + ' criada com sucesso!'

    class Meta:
        verbose_name = 'Linguagem de Programação'
        verbose_name_plural = 'Linguagens de Programação'


class TechSkill(Skill):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, verbose_name='Resume', related_name='tech_skills')

    def get_repr(self) -> str:
        return 'Habilidade Técnica ' + self.name + ' criada com sucesso!'

    class Meta:
        verbose_name = 'Habilidade Técnica'
        verbose_name_plural = 'Habilidades Técnicas'


class SoftSkill(Skill):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, verbose_name='Resume')

    def get_repr(self) -> str:
        return 'Habilidade Leve' + self.name + ' criada com sucesso!'

    class Meta:
        verbose_name = 'Habilidade Leve'
        verbose_name_plural = 'Habilidades Leves'


class CustomSkillCategory(BaseEntity):
    class SkillStyle(models.TextChoices):
        CIRCULAR = 'Circular'
        LINEAR = 'Linear'
        CHECK_MARK = 'Check Mark'

    style = models.CharField(max_length=20, choices=SkillStyle.choices, default=SkillStyle.CHECK_MARK,
                             verbose_name='Estilo')
    name = models.CharField(max_length=50, verbose_name='Nome da Categoria')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, verbose_name='Resume',
                               related_name='custom_skill_categories')
    use_on_resume = models.BooleanField(default=True, verbose_name='Utilizar no Website?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria de Habilidades Personalizada'
        verbose_name_plural = 'Categorias de Habilidades Personalizadas'


class CustomSkillCategorySkill(Skill):
    custom_skill_category = models.ForeignKey(CustomSkillCategory, on_delete=models.CASCADE,
                                              verbose_name='Categoria de Habilidade Personalizada',
                                              related_name='custom_skill_category_skills')

    class Meta:
        verbose_name = 'Habilidade da Categoria Personalizada'
        verbose_name_plural = 'Habilidades da Categoria Personalizada'
