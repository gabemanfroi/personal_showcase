from django.db import models

from apps.blog.models import Blog
from apps.portfolio.models import Portfolio
from apps.resume.models import Resume
from apps.shared.models import BaseEntity, PersonalShowcaseUser


class WebsiteContent(BaseEntity):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE, verbose_name='Resume')
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE, verbose_name='Portfolio', null=True)
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, verbose_name='Blog')
    personal_url = models.CharField(max_length=50, verbose_name='Url pessoal', unique=True)
    background_image = models.ImageField(verbose_name='Imagem do Banner', null=True, blank=True)

    def __str__(self):
        return str(self.created_by) + '\'s' + ' Website'

    class Meta:
        verbose_name = 'Conteúdo do Site'
        verbose_name_plural = verbose_name


class CarrouselItem(BaseEntity):
    title = models.CharField(max_length=60, verbose_name='Item do carrossel do Banner')
    position = models.IntegerField(verbose_name='Posição no carrossel')
    website = models.ForeignKey(WebsiteContent, on_delete=models.CASCADE, verbose_name='Website',
                                related_name='carrousel_items')

    class Meta:
        verbose_name = 'Item do Carrossel (Website Banner)'
        verbose_name_plural = 'Itens do Carrossel (Website Banner)'
