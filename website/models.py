# _*_ coding: utf-8 _*_
from django.db import models
# from django.contrib.gis.db import models   # 空间数据
# from django.contrib.gis.db.models.manager import GeoManager # 空间数据

class DeviceStatus(models.Model):
    name = models.CharField(max_length=50,verbose_name='设备状态分类')

class DeviceGroup(models.Model):
    name = models.CharField(max_length=50,verbose_name='设备分组')

class DeviceRegion(models.Model):
    name = models.CharField(max_length=50,verbose_name='设备分区')

class VideoDirection(models.Model):
    name = models.CharField(max_length=50,verbose_name='摄像头方向')

class VideoType(models.Model):
    name = models.CharField(max_length=32,verbose_name='摄像头分类')

class DeviceBrand(models.Model):
    name = models.CharField(max_length=32,verbose_name='设备品牌')

class DeviceType(models.Model):
    brandid = models.ForeignKey(DeviceBrand,verbose_name='关联设备品牌ID')
    name = models.CharField(max_length=32,verbose_name='设备型号')

class VideoDevice(models.Model):
    pid = models.CharField(max_length=32,verbose_name='摄像头编号',null=True)
    name = models.CharField(max_length=50,verbose_name='摄像头名称')
    group = models.ForeignKey(DeviceGroup,verbose_name='摄像头分组')
    region = models.ForeignKey(DeviceRegion,verbose_name='摄像头区域划分',null=True)
    vtype = models.ForeignKey(VideoType,verbose_name='摄像头类别')
    ip = models.GenericIPAddressField(protocol='ipv4',verbose_name='摄像机IP')
    username = models.CharField(max_length=50,verbose_name='摄像头帐号',null=True)
    password = models.CharField(max_length=50,verbose_name='摄像头密码',null=True)
    gpslon = models.CharField(max_length=18,verbose_name='经度',null=True)
    gpswei = models.CharField(max_length=18,verbose_name='纬度',null=True)

class NVRDevice(models.Manager):
    name = models.CharField(max_length=32,verbose_name='录像机名称')
    ip = models.GenericIPAddressField(protocol='ipv4',verbose_name='录像机IP')
    username = models.CharField(max_length=32,verbose_name='录像机帐号')
    password = models.CharField(max_length=32,verbose_name='录像机密码')

class NetworkDevice(models.Manager):
    name = models.CharField(max_length=32,verbose_name='网络设备名称')
    ip = models.GenericIPAddressField(protocol='ipv4',verbose_name='网络设备IP')
    username = models.CharField(max_length=32,verbose_name='网络设备帐号')
    password = models.CharField(max_length=32,verbose_name='网络设备密码')

class ServerHostDevice(models.Manager):
    name = models.CharField(max_length=32,verbose_name='服务器名称')
    ip = models.GenericIPAddressField(protocol='ipv4',verbose_name='服务器IP')
    username = models.CharField(max_length=32,verbose_name='服务器帐号')
    password = models.CharField(max_length=32,verbose_name='服务器密码')

