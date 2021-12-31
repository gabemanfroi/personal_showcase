# Generated by Django 4.0 on 2021-12-31 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAdditionalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=40, verbose_name='Título')),
                ('description', models.CharField(max_length=60, verbose_name='Descrição')),
            ],
        ),
        migrations.AddField(
            model_name='personalshowcaseuser',
            name='additional_information',
            field=models.ManyToManyField(to='shared.UserAdditionalInformation', verbose_name='Informações Adicionais'),
        ),
    ]
