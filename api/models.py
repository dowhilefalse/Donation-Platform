from django.db import models

# Create your models here.
from registration.models import User


class Organization(models.Model):
    """docstring for Organization"""
    province = models.CharField(verbose_name='省', max_length=32)
    city = models.CharField(verbose_name='市', max_length=32)
    name = models.CharField(verbose_name='名称', max_length=128)
    address = models.TextField(verbose_name='地址', default=None, blank=True, null=True)
    source = models.TextField(verbose_name='数据来源', default=None, blank=True, null=True)
    verified = models.BooleanField(verbose_name='已验证', default=False)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now=True)
    # is_manual, false 即为自动导入, 手动添加的数据优先级更高, 会覆盖同 province，city，name 的数据
    is_manual = models.BooleanField(verbose_name='是否是手动添加', default=False)
    inspector = models.ForeignKey(User, verbose_name='添加人', on_delete=models.CASCADE)
    emergency = models.IntegerField(verbose_name='紧急程度', default=0, null=False)

    def __str__(self):
        """A string representation of the model."""
        return self.name

    class Meta:
        verbose_name = '机构'
        verbose_name_plural = '机构'
        app_label = 'api'

class OrganizationContact(models.Model):
    """docstring for OrganizationContact"""
    organization = models.ForeignKey(Organization, verbose_name='所属机构', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='称呼', max_length=32)
    phone = models.CharField(verbose_name='手机', max_length=31)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now=True)

    def __str__(self):
        """A string representation of the model."""
        return '{0}({1})'.format(self.name, self.phone)

    class Meta:
        verbose_name = '机构联系人'
        verbose_name_plural = '机构联系人'
        app_label = 'api'

class OrganizationDemand(models.Model):
    """docstring for OrganizationDemand"""
    organization = models.ForeignKey(Organization, verbose_name='所属机构', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='物品名', max_length=128)
    remark = models.CharField(verbose_name='备注', max_length=255, default=None, blank=True, null=True)
    amount = models.IntegerField(verbose_name='需求数量', default=-1, null=False) # -1 表示大量(没有具体数字)
    receive_amount = models.IntegerField(verbose_name='收到数量', default=0)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now=True)

    def __str__(self):
        """A string representation of the model."""
        return self.name

    class Meta:
        verbose_name = '机构需求'
        verbose_name_plural = '机构需求'
        app_label = 'api'

# -----------------------------------------------

class Team(models.Model):
    """docstring for Team"""
    name = models.CharField(verbose_name='名称', max_length=128)
    address = models.TextField(verbose_name='所在地', default=None, blank=True, null=True)
    verified = models.BooleanField(verbose_name='已验证', default=False)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now=True)
    main_text = models.TextField(verbose_name='正文', default=None, blank=True, null=True)    
    inspector = models.ForeignKey(User, verbose_name='添加人', on_delete=models.CASCADE)

    def __str__(self):
        """A string representation of the model."""
        return self.name

    class Meta:
        verbose_name = '(爱心)团体'
        verbose_name_plural = '(爱心)团体'
        app_label = 'api'

class TeamContact(models.Model):
    """docstring for TeamContact"""
    team = models.ForeignKey(Team, verbose_name='所属团体', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='称呼', max_length=32)
    phone = models.CharField(verbose_name='手机', max_length=31)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now=True)

    def __str__(self):
        """A string representation of the model."""
        return '{0}({1})'.format(self.name, self.phone)

    class Meta:
        verbose_name = '团体(捐赠)联系人'
        verbose_name_plural = '团体(捐赠)联系人'
        app_label = 'api'