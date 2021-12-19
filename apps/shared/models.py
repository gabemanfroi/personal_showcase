from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Website(BaseEntity):
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


class PersonalShowcaseUser(AbstractUser):
    websites = models.ManyToManyField(to=Website)
