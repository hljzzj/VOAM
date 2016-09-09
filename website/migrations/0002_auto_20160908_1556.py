# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videodevice',
            name='statusid',
            field=models.ForeignKey(verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe7\x8a\xb6\xe6\x80\x81', to='website.DeviceStatus', null=True),
        ),
    ]
