# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 10:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FixedCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixed_cost_percentage', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name=b'Fixed Cost %')),
            ],
        ),
        migrations.CreateModel(
            name='MOQCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moq_category_index', models.IntegerField(default=0, verbose_name=b'MOQ Category Index')),
                ('moq_category', models.CharField(max_length=45, verbose_name=b'MOQ Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaster',
            fields=[
                ('product_code', models.CharField(max_length=45, primary_key=True, serialize=False, verbose_name=b'Product Code')),
                ('product_master_description', models.CharField(max_length=500, verbose_name=b'Product Master Description')),
                ('full_description', models.CharField(max_length=500, verbose_name=b'Full Description')),
                ('vedor_code', models.CharField(max_length=45, verbose_name=b'Vendor Code')),
                ('vendor_moq', models.IntegerField(default=0, verbose_name=b'Vendor MOQ')),
                ('product_type', models.CharField(max_length=45, verbose_name=b'Product Type')),
                ('product_create_date', models.DateTimeField(verbose_name=b'Product Creation Date')),
                ('brand_name', models.CharField(max_length=45, verbose_name=b'Brand Name')),
                ('country_of_origin', models.CharField(max_length=45, verbose_name=b'Country of Origin')),
                ('vendor_prod_lead_time', models.IntegerField(default=0, verbose_name=b'Vendor Production Lead Time')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, verbose_name=b'Category')),
                ('sub_category', models.CharField(max_length=255, verbose_name=b'Sub Category')),
                ('product_group', models.CharField(max_length=255, verbose_name=b'Product Group')),
                ('product_line', models.CharField(max_length=255, verbose_name=b'Product Line')),
                ('product_description', models.CharField(max_length=255, verbose_name=b'Product Description')),
                ('cost_category', models.CharField(max_length=255, verbose_name=b'Cost Category')),
                ('product_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProductMaster')),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buying_office', models.CharField(max_length=45, verbose_name=b'Buying Office')),
                ('sub_buying_office', models.CharField(max_length=45, verbose_name=b'Sub Buying Office')),
                ('operating_company', models.CharField(max_length=45, verbose_name=b'Operating Company')),
                ('fin_month', models.DateTimeField(verbose_name=b'FinMonth')),
                ('order_no', models.CharField(max_length=45, verbose_name=b'Order No')),
                ('order_quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'Order Quantity')),
                ('order_creation_date', models.DateTimeField(verbose_name=b'Order Creation Date')),
                ('request_order_receiving_date', models.DateTimeField(verbose_name=b'Reqyest Order Receiving Date')),
                ('official_order_receiving_date', models.DateTimeField(verbose_name=b'Official Order Receiving Date')),
                ('actual_customer_request_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Actual Customer Request Date')),
                ('actual_order_receiving_date', models.DateTimeField(verbose_name=b'Actual Order Receiving Date')),
                ('order_official_date', models.DateTimeField(verbose_name=b'Order Official Date')),
                ('payment_terms', models.CharField(max_length=45, verbose_name=b'Payment Terms')),
                ('fob', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'FoB')),
                ('shipment_value', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'Shipment Value')),
                ('sku_order_index', models.CharField(max_length=45, verbose_name=b'SKU Order Index')),
                ('vendor_moq', models.IntegerField(default=0, verbose_name=b'Vendor MOQ')),
                ('shipment_value_sku_order', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'Shipment Value SKU Order')),
                ('moq_multiple', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'MOQ Multiple')),
                ('year', models.IntegerField(default=0, verbose_name=b'Year')),
                ('moq_category_index', models.IntegerField(default=0, verbose_name=b'MOQ Category Index')),
                ('moq_category', models.CharField(max_length=45, verbose_name=b'MOQ Category')),
                ('product_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ProductMaster')),
            ],
        ),
        migrations.CreateModel(
            name='VendorList',
            fields=[
                ('vendor_code', models.CharField(max_length=45, primary_key=True, serialize=False, verbose_name=b'Vendor Code')),
                ('vendor_name', models.CharField(max_length=255, verbose_name=b'Vendor Name')),
            ],
        ),
        migrations.CreateModel(
            name='Wage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_of_origin', models.CharField(max_length=45, verbose_name=b'Country of Origin')),
                ('wage_rate', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'Wage Rate ($/hour)')),
            ],
        ),
        migrations.AddField(
            model_name='shipmentdata',
            name='vendor_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.VendorList'),
        ),
        migrations.AddField(
            model_name='fixedcost',
            name='vendor_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.VendorList'),
        ),
    ]