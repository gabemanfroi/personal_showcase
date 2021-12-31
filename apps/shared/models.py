from django.contrib.auth.models import AbstractUser
from django.db import models


class Website(models.Model):
    class WebsiteCategory(models.TextChoices):
        LINKEDIN = 'LinkedIn'
        FACEBOOK = 'Facebook'
        TWITTER = 'Twitter'
        GITHUB = 'Github'
        PORTFOLIO = 'Portfolio'

    category = models.CharField(max_length=20, choices=WebsiteCategory.choices)
    url = models.URLField()

    def get_repr(self) -> str:
        return 'Website criado com sucesso!'

    def __str__(self) -> str:
        return self.category


class UserAdditionalInformation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=40, verbose_name='Título')
    description = models.CharField(max_length=60, verbose_name='Descrição')

    def __str__(self) -> str:
        return self.title


class PersonalShowcaseUser(AbstractUser):
    websites = models.ManyToManyField(Website, blank=True)
    professional_title = models.CharField(max_length=255, verbose_name='Título Profissional')
    additional_information = models.ManyToManyField(UserAdditionalInformation, verbose_name='Informações Adicionais',
                                                    blank=True)
    profile_picture = models.ImageField(verbose_name='Foto de Perfil', blank=True, null=True)


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
