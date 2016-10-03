# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NVRDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\xbd\x95\xe5\x83\x8f\xe6\x9c\xba\xe5\x90\x8d\xe7\xa7\xb0')),
                ('ip', models.GenericIPAddressField(protocol=b'ipv4', verbose_name=b'\xe5\xbd\x95\xe5\x83\x8f\xe6\x9c\xbaIP')),
                ('username', models.CharField(max_length=32, verbose_name=b'\xe5\xbd\x95\xe5\x83\x8f\xe6\x9c\xba\xe5\xb8\x90\xe5\x8f\xb7')),
                ('password', models.CharField(max_length=32, verbose_name=b'\xe5\xbd\x95\xe5\x83\x8f\xe6\x9c\xba\xe5\xaf\x86\xe7\xa0\x81')),
            ],
        ),
    ]
