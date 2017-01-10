"""
Definition of models.
"""

from django.db import models

# Create your models here.
class ProductMaster(models.Model):
    product_code = models.CharField(max_length=50)
    product_master_description = models.CharField(max_length=250)
    full_description = models.CharField(max_length=250)
    vedor_code = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    product_create_date = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50)
    country_of_origin = models.CharField(max_length=50)
    vendor_prod_lead_time = models.CharField(max_length=50)

class ProductStructure(models.Model):
    product_code = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    product_group = models.CharField(max_length=50)
    product_line = models.CharField(max_length=50)
    product_description = models.CharField(max_length=50)
    cost_category = models.CharField(max_length=50)

class ShipmentData(models.Model):
    buying_office = models.CharField(max_length=50)
    sub_buying_office = models.CharField(max_length=50)
    operating_company = models.CharField(max_length=50)
    vendor_code = models.CharField(max_length=50)
    fin_month = models.CharField(max_length=50)
    order_no = models.CharField(max_length=50)
    product_code = models.CharField(max_length=50)
    order_quantity = models.IntegerField()
    order_creation_date = models.DateTimeField()
    request_order_receiving_date = models.DateTimeField()
    official_order_receiving_date = models.DateTimeField()
    actual_customer_receiving_date = models.DateTimeField()
    actual_order_receiving_date = models.DateTimeField()
    order_official_date = models.DateTimeField()
    payment_terms = models.CharField(max_length=250)
    fob = models.CharField(max_length=50)
    shipment_value = models.IntegerField()
    sku_order_index = models.IntegerField()
    vendor_MOQ = models.IntegerField()
    shipment_value_sku_order = models.IntegerField()
    moq_multiple = models.IntegerField()
    year = models.IntegerField()
    moq_category_index = models.IntegerField()
    moq_category = models.IntegerField()

class FixedCost(models.Model):
    vendor_code = models.CharField(max_length=50)
    fixed_cost_percentage = models.IntegerField()

class VendorList(models.Model):
    vendor_code = models.CharField(max_length=50)
    vendor_name = models.CharField(max_length=50)

class MOQCategory(models.Model):
    moq_category_index = models.IntegerField()
    moq_category = models.CharField(max_length=50)