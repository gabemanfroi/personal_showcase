from django.db import models

from apps.shared.models import BaseEntity, PersonalShowcaseUser


class Portfolio(BaseEntity):
    def __str__(self):
        return self.created_by.username + '\'s Portfolio'

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = verbose_name


class Service(BaseEntity):
    title = models.CharField(verbose_name='Serviço', max_length=70)
    description = models.TextField(verbose_name='Descrição do Serviço', max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'


class Project(BaseEntity):
    title = models.CharField(verbose_name='Projeto', max_length=255)
    description = models.TextField(verbose_name='Descrição do Projeto', blank=True, null=True)
    image = models.ImageField(verbose_name='Imagem do Projeto', null=True, blank=True)
    url = models.CharField(verbose_name='URL do Projeto', max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, verbose_name='Portfolio',
                                  related_name='projects')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
