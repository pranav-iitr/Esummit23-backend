# Generated by Django 3.2.6 on 2022-12-26 16:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_alter_otp_date_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='date_expired',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 16, 40, 37, 510035, tzinfo=utc)),
        ),
    ]
