# Generated by Django 4.0.4 on 2022-05-07 20:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userincome', '0002_remove_userincome_quantity_alter_userincome_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userincome',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 7, 20, 48, 11, 891086, tzinfo=utc)),
        ),
    ]
