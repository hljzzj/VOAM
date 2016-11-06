# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20161008_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceFault',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe6\x95\x85\xe9\x9a\x9c\xe5\x8e\x9f\xe5\x9b\xa0')),
            ],
        ),
        migrations.AddField(
            model_name='cameradevice',
            name='faultid',
            field=models.ForeignKey(verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe6\x95\x85\xe9\x9a\x9c\xe5\x8e\x9f\xe5\x9b\xa0', to='website.DeviceFault', null=True),
        ),
    ]
