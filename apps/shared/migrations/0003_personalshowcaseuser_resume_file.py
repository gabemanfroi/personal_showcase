# Generated by Django 4.0 on 2022-01-10 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0002_alter_useradditionalinformation_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalshowcaseuser',
            name='resume_file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Curriculum Vitae'),
        ),
    ]
