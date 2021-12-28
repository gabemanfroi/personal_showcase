# Generated by Django 4.0 on 2021-12-28 02:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='proficiency',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Nível de Proficiência'),
        ),
        migrations.AlterField(
            model_name='programminglanguage',
            name='proficiency',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Nível de Proficiência'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='work_experiences',
            field=models.ManyToManyField(blank=True, to='resume.WorkExperience'),
        ),
        migrations.AlterField(
            model_name='softskill',
            name='proficiency',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Nível de Proficiência'),
        ),
        migrations.AlterField(
            model_name='techskill',
            name='proficiency',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Nível de Proficiência'),
        ),
    ]
