# Generated by Django 2.1.7 on 2019-03-07 05:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0002_salary_doj'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='email',
            field=models.EmailField(default='abcd@gmail.com', max_length=40, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='doj',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 7, 5, 33, 4, 168181, tzinfo=utc)),
        ),
    ]