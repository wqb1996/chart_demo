# Generated by Django 3.0.8 on 2020-07-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbdata', '0003_auto_20200711_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartinfo',
            name='CLM',
            field=models.TextField(null=True, verbose_name='CLM：专利权利要求'),
        ),
    ]