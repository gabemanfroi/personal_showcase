from django.db import models

from apps.shared.models import BaseEntity


class Subject(BaseEntity):
    title = models.CharField(verbose_name='Título', max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Assunto'
        verbose_name_plural = 'Assuntos'


class Topic(BaseEntity):
    title = models.CharField(verbose_name='Título', max_length=255)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Tópico'
        verbose_name_plural = 'Tópicos'


class Step(BaseEntity):
    position = models.IntegerField(verbose_name='Posição')
    title = models.CharField(verbose_name='Título', max_length=255)
    topic = models.ForeignKey(to=Topic, on_delete=models.CASCADE, verbose_name='Tópico')
    source_code = models.FileField(verbose_name='Código Fonte')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Passo'
        verbose_name_plural = 'Passos'
