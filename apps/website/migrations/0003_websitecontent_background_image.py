# Generated by Django 4.0 on 2022-01-01 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_carrouselitem_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitecontent',
            name='background_image',
            field=models.ImageField(default='', upload_to='', verbose_name='Imagem do Banner'),
            preserve_default=False,
        ),
    ]
