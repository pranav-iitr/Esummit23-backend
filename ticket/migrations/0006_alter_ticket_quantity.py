# Generated by Django 3.2.6 on 2023-02-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_alter_ticket_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantity'),
        ),
    ]
