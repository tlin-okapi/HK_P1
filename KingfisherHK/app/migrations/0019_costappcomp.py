# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-17 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_moqcategory_moq_savings'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostAppComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=45, verbose_name=b'Product Type')),
                ('final_cost', models.FloatField(default=0, verbose_name=b'Final Cost')),
            ],
        ),
    ]
