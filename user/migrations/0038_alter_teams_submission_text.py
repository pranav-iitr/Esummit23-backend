# Generated by Django 3.2.6 on 2023-01-18 11:23

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0037_teams_submission_text2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='submission_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
    ]
