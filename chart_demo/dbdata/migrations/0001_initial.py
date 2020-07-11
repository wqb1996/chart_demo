# Generated by Django 3.0.8 on 2020-07-11 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_id', models.CharField(max_length=1000, null=True, verbose_name='专利的唯一标识')),
                ('PA', models.CharField(max_length=1000, null=True, verbose_name='申请人')),
                ('AD', models.CharField(max_length=1000, null=True, verbose_name='申请日')),
                ('PD', models.CharField(max_length=1000, null=True, verbose_name='公开日')),
                ('TI', models.CharField(max_length=1000, null=True, verbose_name='标题')),
                ('LS', models.CharField(max_length=1000, null=True, verbose_name='法律状态')),
                ('CDN', models.CharField(max_length=1000, null=True, verbose_name='被引证专利号')),
                ('CTN', models.CharField(max_length=1000, null=True, verbose_name='CTN：引证专利号')),
                ('AN', models.CharField(max_length=1000, null=True, verbose_name='AN：申请号')),
                ('IPC', models.CharField(max_length=1000, null=True, verbose_name='IPC：国际专利分类号')),
                ('PN', models.CharField(max_length=1000, null=True, verbose_name='PN：公开号')),
                ('LSE', models.CharField(max_length=1000, null=True, verbose_name='LSE：历史法律事件')),
                ('AB', models.CharField(max_length=1000, null=True, verbose_name='AB：专利摘要')),
                ('CLM', models.CharField(max_length=1000, null=True, verbose_name='CLM：专利权利要求')),
            ],
            options={
                'verbose_name': '图标数据',
                'verbose_name_plural': '图标数据',
                'db_table': 'tb_chartinfo',
            },
        ),
    ]