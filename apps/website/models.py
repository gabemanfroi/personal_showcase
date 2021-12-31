from django.db import models

from apps.portfolio.models import Portfolio
from apps.resume.models import Resume
from apps.shared.models import BaseEntity, PersonalShowcaseUser


class CarrouselItem(BaseEntity):
    title = models.CharField(max_length=60, verbose_name='Item do carrossel do Banner')
    position = models.IntegerField(verbose_name='Posição no carrossel')

    class Meta:
        verbose_name = 'Item do Carrossel (Website Banner)'
        verbose_name_plural = 'Itens do Carrossel (Website Banner)'


class WebsiteContent(BaseEntity):
    user = models.ForeignKey(PersonalShowcaseUser, on_delete=models.CASCADE, verbose_name='Usuário')
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE, verbose_name='Resume')
    carrousel_items = models.ManyToManyField(CarrouselItem, verbose_name='Itens do Carrossel')
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE, verbose_name='Portfolio', null=True)

    class Meta:
        verbose_name = 'Conteúdo do Site'
