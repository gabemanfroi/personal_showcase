# Generated by Django 4.0 on 2022-01-01 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name': 'Projeto', 'verbose_name_plural': 'Projeto'},
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='projects',
        ),
        migrations.AddField(
            model_name='project',
            name='portfolio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='portfolio.portfolio', verbose_name='Portfolio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição do Projeto'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Descrição do Serviço'),
        ),
    ]