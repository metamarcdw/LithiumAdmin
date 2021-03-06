# Generated by Django 2.2.8 on 2020-01-10 14:15

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
                ('name', models.CharField(max_length=100)),
                ('prod_hosting', models.CharField(choices=[('ONP', 'On-Premise'), ('HOS', 'Hosted'), ('SAA', 'SaaS')], default='SAA', max_length=3)),
                ('prod_version', models.CharField(max_length=10)),
                ('salesforce_name', models.CharField(max_length=100, unique=True)),
                ('database_type', models.CharField(blank=True, choices=[('OR', 'Oracle'), ('MS', 'SQL Server')], default='OR', max_length=2)),
                ('datacenter', models.CharField(blank=True, choices=[('SF', 'Southfield'), ('LV', 'Las Vegas'), ('EU', 'Amsterdam'), ('CA', 'Calgary')], default='SF', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='KnownBug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jira_case', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField()),
                ('affected_versions', models.CharField(max_length=100)),
                ('fix_versions', models.CharField(default='Not fixed', max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('salesforce_case', models.CharField(max_length=10, unique=True)),
                ('date_entered', models.DateField(auto_now_add=True)),
                ('date_requested', models.DateField()),
                ('status', models.CharField(choices=[('QUE', 'Queued with Lithium'), ('INP', 'In Progress'), ('NOT', 'Waiting on another Team'), ('CLO', 'Closed / Resolved')], default='QUE', max_length=3)),
                ('priority', models.CharField(choices=[('CRI', 'Critical'), ('HI', 'High'), ('MED', 'Medium'), ('LOW', 'Low')], default='MED', max_length=3)),
                ('severity', models.CharField(choices=[('SEV1', 'Severity 1'), ('SEV2', 'Severity 2'), ('SEV3', 'Severity 3'), ('SEVN', 'None')], default='SEV3', max_length=4)),
                ('is_billable', models.BooleanField(default=False)),
                ('project_code', models.CharField(blank=True, max_length=20)),
                ('files_location', models.CharField(blank=True, max_length=300)),
                ('customer_notes', models.TextField()),
                ('analyst_notes', models.TextField(blank=True)),
                ('developer_notes', models.TextField(blank=True)),
                ('my_notes', models.TextField(blank=True)),
                ('report_me', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_cases', to='lithiumadmin.Customer')),
                ('associated_bug', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bug_cases', to='lithiumadmin.KnownBug')),
            ],
        ),
    ]
