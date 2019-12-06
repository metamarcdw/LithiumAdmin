# Generated by Django 2.2.8 on 2019-12-05 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('prod_hosting', models.CharField(choices=[('ONP', 'On-Premise'), ('HOS', 'Hosted'), ('SAA', 'SaaS')], default='SAA', max_length=3)),
                ('prod_version', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entered', models.DateField(auto_now_add=True)),
                ('date_requested', models.DateField()),
                ('status', models.CharField(choices=[('QUE', 'Queued with Lithium'), ('INP', 'In Progress'), ('NOT', 'Waiting on another Team'), ('CLO', 'Closed or Resolved')], default='QUE', max_length=3)),
                ('priority', models.CharField(choices=[('LOW', 'Low'), ('MED', 'Medium'), ('HI', 'High'), ('CRI', 'Critical')], default='MED', max_length=3)),
                ('severity', models.CharField(choices=[('SEV1', 'Severity 1'), ('SEV2', 'Severity 2'), ('SEV3', 'Severity 3')], default='SEV3', max_length=4)),
                ('is_billable', models.BooleanField(default=False)),
                ('project_code', models.CharField(blank=True, max_length=20)),
                ('customer_notes', models.TextField()),
                ('analyst_notes', models.TextField(blank=True)),
                ('my_notes', models.TextField(blank=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lithiumadmin.Customer')),
            ],
        ),
    ]
