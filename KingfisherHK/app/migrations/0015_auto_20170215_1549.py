# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_shipmentcalc_tsp_moq'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipmentcalc',
            name='TSP_CostRecovery',
            field=models.FloatField(default=0, verbose_name=b'Theoretical Saving Potential - Cost Recovery'),
        ),
        migrations.AddField(
            model_name='shipmentcalc',
            name='TSP_MOT',
            field=models.FloatField(default=0, verbose_name=b'Theoretical Saving Potential - Money On the Table'),
        ),
    ]
