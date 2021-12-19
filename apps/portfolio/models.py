from django.db import models

from apps.shared.models import BaseEntity


class Project(BaseEntity):
    title = models.CharField(verbose_name='Projeto', max_length=255)
    description = models.TextField(verbose_name='Descrição do Projeto')
    image = models.ImageField(verbose_name='Imagem do Projeto', null=True, blank=True)
    url = models.CharField(verbose_name='URL do Projeto', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
