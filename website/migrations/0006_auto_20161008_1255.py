# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20161004_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='PowerSupply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe4\xbe\x9b\xe7\x94\xb5\xe6\x96\xb9\xe5\xbc\x8f')),
            ],
        ),
        migrations.AddField(
            model_name='cameradevice',
            name='powerid',
            field=models.CharField(max_length=32, null=True, verbose_name=b'\xe4\xbe\x9b\xe7\x94\xb5\xe6\xa0\x87\xe8\xaf\x86'),
        ),
    ]
