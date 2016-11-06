# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20161106_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='PowerID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe4\xbe\x9b\xe7\x94\xb5\xe6\xa0\x87\xe8\xaf\x86')),
            ],
        ),
        migrations.AddField(
            model_name='cameradevice',
            name='powersupplyid',
            field=models.ForeignKey(verbose_name=b'\xe4\xbe\x9b\xe7\x94\xb5\xe6\x96\xb9\xe5\xbc\x8f', to='website.PowerSupply', null=True),
        ),
        migrations.AlterField(
            model_name='cameradevice',
            name='powerid',
            field=models.ForeignKey(verbose_name=b'\xe4\xbe\x9b\xe7\x94\xb5\xe6\xa0\x87\xe8\xaf\x86', to='website.PowerID', null=True),
        ),
    ]
