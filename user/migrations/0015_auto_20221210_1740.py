# Generated by Django 3.2.6 on 2022-12-10 12:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_alter_services_options'),
        ('user', '0014_alter_otp_date_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='causer',
            name='Services',
            field=models.ManyToManyField(blank=True, to='events.Services'),
        ),
        migrations.AddField(
            model_name='proffuser',
            name='Services',
            field=models.ManyToManyField(blank=True, to='events.Services'),
        ),
        migrations.AddField(
            model_name='startupuser',
            name='Services',
            field=models.ManyToManyField(blank=True, to='events.Services'),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='Services',
            field=models.ManyToManyField(blank=True, to='events.Services'),
        ),
        migrations.AlterField(
            model_name='otp',
            name='date_expired',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 10, 12, 40, 31, 806458, tzinfo=utc)),
        ),
    ]
