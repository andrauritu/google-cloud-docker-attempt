# Generated by Django 5.0.7 on 2024-09-09 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_rename_title_project_name_remove_project_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='subtitle',
            field=models.CharField(default='Not specified', max_length=100),
        ),
    ]
