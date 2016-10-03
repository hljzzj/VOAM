# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_nvrdevice'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe8\xae\xbe\xe5\xa4\x87\xe5\x90\x8d\xe7\xa7\xb0')),
                ('ip', models.GenericIPAddressField(protocol=b'ipv4', verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe8\xae\xbe\xe5\xa4\x87IP')),
                ('username', models.CharField(max_length=32, verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe8\xae\xbe\xe5\xa4\x87\xe5\xb8\x90\xe5\x8f\xb7')),
                ('password', models.CharField(max_length=32, verbose_name=b'\xe7\xbd\x91\xe7\xbb\x9c\xe8\xae\xbe\xe5\xa4\x87\xe5\xaf\x86\xe7\xa0\x81')),
            ],
        ),
        migrations.CreateModel(
            name='ServerHostDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('ip', models.GenericIPAddressField(protocol=b'ipv4', verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8IP')),
                ('username', models.CharField(max_length=32, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\xb8\x90\xe5\x8f\xb7')),
                ('password', models.CharField(max_length=32, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\xaf\x86\xe7\xa0\x81')),
            ],
        ),
    ]
