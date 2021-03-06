# Generated by Django 2.2.8 on 2021-01-22 17:50

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('EventName', models.CharField(max_length=50)),
                ('Desc', models.TextField(blank=True, max_length=50)),
                ('Loc', models.CharField(max_length=32)),
                ('FromDate', models.DateField(default=datetime.date.today)),
                ('FromTime', models.TimeField(default=django.utils.timezone.now)),
                ('ToDate', models.DateField(default=datetime.date.today)),
                ('ToTime', models.TimeField(default=django.utils.timezone.now)),
                ('RegEndDate', models.DateField(default=datetime.date.today)),
                ('RegEndTime', models.TimeField(default=django.utils.timezone.now)),
                ('HostEmail', models.EmailField(max_length=254)),
                ('HostPassword', models.CharField(max_length=32)),
                ('Status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Contact', models.PositiveIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('EventReg', models.CharField(max_length=50)),
                ('RegType', models.CharField(choices=[('Individual', 'Individual'), ('Group', 'Group')], default='Individual', max_length=32)),
                ('Number', models.IntegerField()),
            ],
        ),
    ]
