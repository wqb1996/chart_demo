# Generated by Django 3.0.8 on 2020-07-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbdata', '0004_auto_20200711_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartinfo',
            name='CDN',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='被引证专利号'),
        ),
    ]
