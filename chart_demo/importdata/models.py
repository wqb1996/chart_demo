from django.db import models


class PatentAuthor(models.Model):
    name = models.CharField(max_length=20)


class InterPatentCode(models.Model):
    code = models.CharField(max_length=10)
    firstcode = models.CharField(max_length=10)
    seccode = models.CharField(max_length=10)


class LawStatusEvent(models.Model):
    name = models.CharField(max_length=20)


class PatentCode(models.Model):
    code = models.CharField(max_length=30)

class Patent(models.Model):
    pid = models.CharField(max_length=64)
    an = models.CharField(max_length=20)
    pn = models.CharField(max_length=20)
    ti = models.CharField(max_length=100)
    ls = models.CharField(max_length=5)

    ad = models.DateField()
    pd = models.DateField()
    ab = models.TextField()
    clm = models.TextField()

    pa = models.ManyToManyField('PatentAuthor')
    ipc = models.ManyToManyField('InterPatentCode')
    lse = models.ManyToManyField('LawStatusEvent')
    ctn = models.ManyToManyField('PatentCode', related_name='ctnpatent')
    cdn = models.ManyToManyField('PatentCode', related_name='cdnpatent')
