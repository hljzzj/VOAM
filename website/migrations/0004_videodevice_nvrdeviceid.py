# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_networkdevice_serverhostdevice'),
    ]

    operations = [
        migrations.AddField(
            model_name='videodevice',
            name='nvrdeviceid',
            field=models.ForeignKey(verbose_name=b'\xe5\x90\x8e\xe5\x8f\xb0\xe5\xad\x98\xe5\x82\xa8\xe8\xae\xbe\xe5\xa4\x87', to='website.NVRDevice', null=True),
        ),
    ]
