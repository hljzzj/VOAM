# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_videodevice_nvrdeviceid'),
    ]

    operations = [
        migrations.CreateModel(
            name='CameraDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pid', models.CharField(max_length=32, null=True, verbose_name=b'\xe6\x91\x84\xe5\x83\x8f\xe5\xa4\xb4\xe7\xbc\x96\xe5\x8f\xb7')),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe6\x91\x84\xe5\x83\x8f\xe5\xa4\xb4\xe5\x90\x8d\xe7\xa7\xb0')),
                ('ip', models.GenericIPAddressField(protocol=b'ipv4', verbose_name=b'\xe6\x91\x84\xe5\x83\x8f\xe6\x9c\xbaIP')),
                ('username', models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x91\x84\xe5\x83\x8f\xe5\xa4\xb4\xe5\xb8\x90\xe5\x8f\xb7')),
                ('password', models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x91\x84\xe5\x83\x8f\xe5\xa4\xb4\xe5\xaf\x86\xe7\xa0\x81')),
                ('gpslon', models.CharField(max_length=18, null=True, verbose_name=b'\xe7\xbb\x8f\xe5\xba\xa6')),
                ('gpswei', models.CharField(max_length=18, null=True, verbose_name=b'\xe7\xba\xac\xe5\xba\xa6')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('brandid', models.ForeignKey(verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe5\x93\x81\xe7\x89\x8c', to='website.DeviceBrand')),
            ],
        ),
        migrations.RenameModel(
            old_name='VideoDirection',
            new_name='CameraDirection',
        ),
        migrations.RenameModel(
            old_name='VideoType',
            new_name='CameraType',
        ),
        migrations.RemoveField(
            model_name='videodevice',
            name='brandid',
        ),
        migrations.RemoveField(
            model_name='videodevice',
            name='directionid',
        ),
        migrations.RemoveField(
            model_name='videodevice',
            name='dtypeid',
        ),
        migrations.RemoveField(
            model_name='videodevice',
            name='groupid',
        ),
        migrations.RemoveField(
            model_name='videodevice',
            name='nvrdeviceid',
        ),
        migrations.RemoveField(
            model_name='videodevice',
            name='regionid',
        ),
        migrations.RemoveField(
            model_name='videodevice',
            name='statusid',
        ),
        migrations.RemoveField(
            model_name='videodevice',
            name='telecomid',
        ),
        migrations.RemoveField(
            model_name='videodevice',
            name='vtypeid',
        ),
        migrations.DeleteModel(
            name='VideoDevice',
        ),
        migrations.AddField(
            model_name='cameradevice',
            name='ctypeid',
            field=models.ForeignKey(verbose_name=b'\xe6\x91\x84\xe5\x83\x8f\xe5\xa4\xb4\xe7\xb1\xbb\xe5\x88\xab', to='website.CameraType'),
        ),
        migrations.AddField(
            model_name='cameradevice',
            name='directionid',
            field=models.ForeignKey(verbose_name=b'\xe6\x91\x84\xe5\x83\x8f\xe5\xa4\xb4\xe6\x96\xb9\xe5\x90\x91', to='website.CameraDirection'),
        ),
        migrations.AddField(
            model_name='cameradevice',
            name='dtypeid',
            field=models.ForeignKey(verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe5\x9e\x8b\xe5\x8f\xb7', to='website.DeviceType'),
        ),
        migrations.AddField(
            model_name='cameradevice',
            name='groupid',
            field=models.ForeignKey(verbose_name=b'\xe6\x91\x84\xe5\x83\x8f\xe5\xa4\xb4\xe5\x88\x86\xe7\xbb\x84', to='website.DeviceGroup'),
        ),
        migrations.AddField(
            model_name='cameradevice',
            name='nvrdeviceid',
            field=models.ForeignKey(verbose_name=b'\xe5\x90\x8e\xe5\x8f\xb0\xe5\xad\x98\xe5\x82\xa8\xe8\xae\xbe\xe5\xa4\x87', to='website.NVRDevice', null=True),
        ),
        migrations.AddField(
            model_name='cameradevice',
            name='regionid',
            field=models.ForeignKey(verbose_name=b'\xe6\x91\x84\xe5\x83\x8f\xe5\xa4\xb4\xe5\x8c\xba\xe5\x9f\x9f\xe5\x88\x92\xe5\x88\x86', to='website.DeviceRegion'),
        ),
        migrations.AddField(
            model_name='cameradevice',
            name='statusid',
            field=models.ForeignKey(verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe7\x8a\xb6\xe6\x80\x81', to='website.DeviceStatus', null=True),
        ),
        migrations.AddField(
            model_name='cameradevice',
            name='telecomid',
            field=models.ForeignKey(verbose_name=b'\xe8\xbf\x90\xe8\x90\xa5\xe5\x95\x86', to='website.Telecom'),
        ),
    ]
