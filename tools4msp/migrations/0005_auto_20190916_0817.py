# Generated by Django 2.2.2 on 2019-09-16 08:17

from django.db import migrations, models
import django.db.models.deletion
import tools4msp.models


class Migration(migrations.Migration):

    dependencies = [
        ('tools4msp', '0004_auto_20190914_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudyinput',
            name='coded_label',
            field=models.ForeignKey(limit_choices_to={'group__in': ['casestudy', 'pre', 'env', 'use', 'out']}, on_delete=django.db.models.deletion.CASCADE, to='tools4msp.CodedLabel'),
        ),
        migrations.AlterField(
            model_name='casestudylayer',
            name='coded_label',
            field=models.ForeignKey(limit_choices_to={'group__in': ['casestudy', 'pre', 'env', 'use', 'out']}, on_delete=django.db.models.deletion.CASCADE, to='tools4msp.CodedLabel'),
        ),
        migrations.AlterField(
            model_name='casestudyruninput',
            name='coded_label',
            field=models.ForeignKey(limit_choices_to={'group__in': ['casestudy', 'pre', 'env', 'use', 'out']}, on_delete=django.db.models.deletion.CASCADE, to='tools4msp.CodedLabel'),
        ),
        migrations.AlterField(
            model_name='casestudyrunlayer',
            name='coded_label',
            field=models.ForeignKey(limit_choices_to={'group__in': ['casestudy', 'pre', 'env', 'use', 'out']}, on_delete=django.db.models.deletion.CASCADE, to='tools4msp.CodedLabel'),
        ),
        migrations.AlterField(
            model_name='casestudyrunoutput',
            name='coded_label',
            field=models.ForeignKey(limit_choices_to={'group__in': ['casestudy', 'pre', 'env', 'use', 'out']}, on_delete=django.db.models.deletion.CASCADE, to='tools4msp.CodedLabel'),
        ),
        migrations.AlterField(
            model_name='casestudyrunoutputlayer',
            name='coded_label',
            field=models.ForeignKey(limit_choices_to={'group__in': ['casestudy', 'pre', 'env', 'use', 'out']}, on_delete=django.db.models.deletion.CASCADE, to='tools4msp.CodedLabel'),
        ),
        migrations.CreateModel(
            name='CaseStudyRunGraphic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=tools4msp.models.generate_filename)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('casestudy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='graphics', to='tools4msp.CaseStudyRun')),
                ('coded_label', models.ForeignKey(limit_choices_to={'group__in': ['casestudy', 'pre', 'env', 'use', 'out']}, on_delete=django.db.models.deletion.CASCADE, to='tools4msp.CodedLabel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CaseStudyGraphic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=tools4msp.models.generate_filename)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('casestudy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='graphics', to='tools4msp.CaseStudy')),
                ('coded_label', models.ForeignKey(limit_choices_to={'group__in': ['casestudy', 'pre', 'env', 'use', 'out']}, on_delete=django.db.models.deletion.CASCADE, to='tools4msp.CodedLabel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
