# Generated by Django 2.2.8 on 2019-12-18 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lithiumadmin', '0006_auto_20191218_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='salesforce_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
