# Generated by Django 2.2.2 on 2019-07-03 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools4msp', '0008_auto_20190703_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casestudy',
            old_name='grid',
            new_name='domain_area_dataset',
        ),
    ]