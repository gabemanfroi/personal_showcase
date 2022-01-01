from django.contrib.auth.models import AbstractUser
from django.db import models


class PersonalShowcaseUser(AbstractUser):
    professional_title = models.CharField(max_length=255, verbose_name='Título Profissional')
    profile_picture = models.ImageField(verbose_name='Foto de Perfil', blank=True, null=True)

    def get_repr(self) -> str:
        return 'Usuário criado com sucesso!'

    def __str__(self) -> str:
        return self.username


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(PersonalShowcaseUser, on_delete=models.CASCADE, verbose_name='Usuário')

    class Meta:
        abstract = True


class UserAdditionalInformation(BaseEntity):
    title = models.CharField(max_length=40, verbose_name='Título')
    description = models.CharField(max_length=60, verbose_name='Descrição')
    created_by = models.ForeignKey(PersonalShowcaseUser, on_delete=models.CASCADE, verbose_name='Usuário',
                                   related_name='additional_information')

    def __str__(self) -> str:
        return self.title


class Website(BaseEntity):
    class WebsiteCategory(models.TextChoices):
        LINKEDIN = 'LinkedIn'
        FACEBOOK = 'Facebook'
        TWITTER = 'Twitter'
        GITHUB = 'Github'
        PORTFOLIO = 'Portfolio'

    created_by = models.ForeignKey(PersonalShowcaseUser, on_delete=models.CASCADE, verbose_name='Usuário',
                                   related_name='websites')

    category = models.CharField(max_length=20, choices=WebsiteCategory.choices)
    url = models.URLField()
