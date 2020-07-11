from django.db import models


class ChartInfo(models.Model):
    b_id = models.CharField(max_length=1000, verbose_name="专利的唯一标识", null=True, blank=True)
    PA = models.CharField(max_length=1000, verbose_name="申请人", null=True, blank=True)
    AD = models.CharField(max_length=1000, verbose_name="申请日", null=True, blank=True)
    PD = models.CharField(max_length=1000, verbose_name="公开日", null=True, blank=True)
    TI = models.CharField(max_length=1000, verbose_name="标题", null=True, blank=True)
    LS = models.CharField(max_length=1000, verbose_name="法律状态", null=True, blank=True)
    CDN = models.CharField(max_length=1000, verbose_name="被引证专利号", null=True, default='', blank=True)
    CTN = models.CharField(max_length=1000, verbose_name="CTN：引证专利号", null=True, blank=True)
    AN = models.CharField(max_length=1000, verbose_name="AN：申请号", null=True, blank=True)
    IPC = models.CharField(max_length=1000, verbose_name="IPC：国际专利分类号", null=True, blank=True)
    PN = models.CharField(max_length=1000, verbose_name="PN：公开号", null=True, blank=True)
    LSE = models.CharField(max_length=1000, verbose_name="LSE：历史法律事件", null=True, blank=True)
    AB = models.TextField(verbose_name="AB：专利摘要", null=True, blank=True)
    CLM = models.TextField(verbose_name="CLM：专利权利要求", null=True, blank=True)

    class Meta:
        db_table = 'tb_chartinfo'
        verbose_name = '图标数据'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.b_id
