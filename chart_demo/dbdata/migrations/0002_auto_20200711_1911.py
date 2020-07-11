# Generated by Django 3.0.8 on 2020-07-11 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartinfo',
            name='CDN',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='被引证专利号'),
        ),
        migrations.AlterField(
            model_name='chartinfo',
            name='CLM',
            field=models.CharField(max_length=2000, null=True, verbose_name='CLM：专利权利要求'),
        ),
    ]
