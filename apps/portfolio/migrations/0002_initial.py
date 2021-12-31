# Generated by Django 4.0 on 2021-12-28 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolio', '0001_initial'),
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.personalshowcaseuser'),
        ),
        migrations.AddField(
            model_name='project',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.service'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='projects',
            field=models.ManyToManyField(to='portfolio.Project', verbose_name='Projetos'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shared.personalshowcaseuser'),
        ),
    ]