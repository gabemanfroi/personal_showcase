# Generated by Django 4.0 on 2021-12-28 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
            ],
            options={
                'verbose_name': 'Assunto',
                'verbose_name_plural': 'Assuntos',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn_me.subject')),
            ],
            options={
                'verbose_name': 'Tópico',
                'verbose_name_plural': 'Tópicos',
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('position', models.IntegerField(verbose_name='Posição')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('source_code', models.FileField(upload_to='', verbose_name='Código Fonte')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn_me.topic', verbose_name='Tópico')),
            ],
            options={
                'verbose_name': 'Passo',
                'verbose_name_plural': 'Passos',
            },
        ),
    ]
