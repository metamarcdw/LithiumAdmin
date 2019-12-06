# Generated by Django 2.2.8 on 2019-12-06 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lithiumadmin', '0002_auto_20191205_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='report_me',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='case',
            name='priority',
            field=models.CharField(choices=[('CRI', 'Critical'), ('HI', 'High'), ('MED', 'Medium'), ('LOW', 'Low')], default='MED', max_length=3),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('QUE', 'Queued with Lithium'), ('INP', 'In Progress'), ('NOT', 'Waiting on another Team'), ('CLO', 'Closed / Resolved')], default='QUE', max_length=3),
        ),
    ]
