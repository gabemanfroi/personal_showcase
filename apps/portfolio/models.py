from django.db import models

from apps.shared.models import BaseEntity, PersonalShowcaseUser


class Service(BaseEntity):
    title = models.CharField(verbose_name='Serviço', max_length=70)
    description = models.TextField(verbose_name='Descrição do Serviço', max_length=255)
    user = models.ForeignKey(PersonalShowcaseUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'


class Project(BaseEntity):
    title = models.CharField(verbose_name='Projeto', max_length=255)
    description = models.TextField(verbose_name='Descrição do Projeto')
    image = models.ImageField(verbose_name='Imagem do Projeto', null=True, blank=True)
    url = models.CharField(verbose_name='URL do Projeto', max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'


class Portfolio(BaseEntity):
    projects = models.ManyToManyField(Project, verbose_name='Projetos')
    user = models.OneToOneField(PersonalShowcaseUser, on_delete=models.CASCADE)
