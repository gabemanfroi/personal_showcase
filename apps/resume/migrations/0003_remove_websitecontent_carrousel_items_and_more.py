# Generated by Django 4.0 on 2021-12-30 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websitecontent',
            name='carrousel_items',
        ),
        migrations.RemoveField(
            model_name='websitecontent',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='websitecontent',
            name='user',
        ),
        migrations.DeleteModel(
            name='CarrouselItem',
        ),
        migrations.DeleteModel(
            name='WebsiteContent',
        ),
    ]
