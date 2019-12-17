from django.db import models


class Student(models.Model):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '未知'),
    ]
    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝'),
    ]
    name = models.CharField(max_length=128, verbose_name='姓名')
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name='性别')
    profession = models.CharField(max_length=128, verbose_name='职业')
    email = models.EmailField(verbose_name='Email')
    qq = models.CharField(max_length=12, verbose_name='QQ')
    phone = models.CharField(max_length=11, verbose_name='电话')
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name='审核状态')
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间')

    def __str__(self):
        return '<Student: %s>' % self.name

    class Meta:
        verbose_name = verbose_name_plural = '学员信息'

    @property
    def sex_show(self):
        return dict(self.SEX_ITEMS).get(self.sex)

    @classmethod
    def get_all(cls):
        return cls.objects.all()
