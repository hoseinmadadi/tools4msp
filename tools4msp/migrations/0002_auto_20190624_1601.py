# Generated by Django 2.2.2 on 2019-06-24 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools4msp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudy',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 6, 24, 16, 1, 30, 921328)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='casestudy',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]