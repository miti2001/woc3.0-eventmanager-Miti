# Generated by Django 2.2.8 on 2021-01-31 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commune', '0004_auto_20210131_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Category',
            field=models.CharField(choices=[('Seminar', 'Seminar'), ('Workshop', 'Workshop'), ('Festival', 'Festival'), ('Competition', 'Competition'), ('Other', 'Other')], default='Other', max_length=32),
        ),
    ]