from django.db import models

from apps.shared.models import BaseEntity


class Subject(BaseEntity):
    title = models.CharField(verbose_name='Título', max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Assunto'
        verbose_name_plural = 'Assuntos'


class Article(BaseEntity):
    subjects = models.ManyToManyField(to=Subject)
    title = models.CharField(verbose_name='Título', max_length=255)
    content = models.TextField(verbose_name='Conteúdo')
    image = models.ImageField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
