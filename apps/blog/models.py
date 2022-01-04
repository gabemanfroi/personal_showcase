from django.db import models

from apps.shared.models import BaseEntity, PersonalShowcaseUser


class Subject(BaseEntity):
    title = models.CharField(verbose_name='Título', max_length=255)
    created_by = models.ForeignKey(PersonalShowcaseUser, on_delete=models.CASCADE, verbose_name='Usuário',
                                   related_name='%(class)s_created_by')
    tag_color = models.CharField(verbose_name="Cor da Tag", max_length=9)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Assunto'
        verbose_name_plural = 'Assuntos'


class Blog(BaseEntity):
    def __str__(self):
        return self.created_by.username + '\'s Blog'

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = verbose_name


class Article(BaseEntity):
    subjects = models.ManyToManyField(to=Subject)
    title = models.CharField(verbose_name='Título', max_length=255)
    content = models.TextField(verbose_name='Conteúdo')
    image = models.ImageField(blank=True, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='articles')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
