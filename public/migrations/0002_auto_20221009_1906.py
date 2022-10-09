# Generated by Django 3.2.6 on 2022-10-09 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speakers',
            old_name='date',
            new_name='date_event',
        ),
        migrations.RenameField(
            model_name='speakers',
            old_name='time',
            new_name='time_event',
        ),
        migrations.AlterField(
            model_name='speakers',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='speakers/', verbose_name='Speaker Image'),
        ),
    ]
