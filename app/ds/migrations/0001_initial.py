# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diseases', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symptoms', models.CharField(max_length=20)),
                ('disease', models.ForeignKey(to='ds.Diseases')),
            ],
        ),
    ]
