# Generated by Django 2.2.8 on 2019-12-18 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lithiumadmin', '0005_auto_20191218_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knownbug',
            name='fix_versions',
            field=models.CharField(default='Not fixed', max_length=100),
        ),
    ]