"""
Definition of models.
"""

from django.db import models
from django.utils import timezone

# Create your models here.
class ProductMaster(models.Model):
    product_code = models.CharField(verbose_name='Product Code', max_length=45, primary_key=True)
    product_master_description = models.CharField(verbose_name='Product Master Description', max_length=500)
    full_description = models.CharField(verbose_name='Full Description', max_length=500)
    vendor_code = models.CharField(verbose_name='Vendor Code', max_length=45)
    vendor_moq = models.IntegerField(verbose_name='Vendor MOQ', default = 0)
    product_type = models.CharField(verbose_name='Product Type', max_length=45)
    product_create_date = models.DateTimeField(verbose_name='Product Creation Date')
    brand_name = models.CharField(verbose_name='Brand Name', max_length=45)
    country_of_origin = models.CharField(verbose_name='Country of Origin', max_length=45)
    vendor_prod_lead_time = models.IntegerField(verbose_name='Vendor Production Lead Time', default = 0)
    

class ProductStructure(models.Model):
    product_code = models.ForeignKey(ProductMaster, on_delete=models.CASCADE)
    category = models.CharField(verbose_name='Category', max_length=255)
    sub_category = models.CharField(verbose_name='Sub Category', max_length=255)
    product_group = models.CharField(verbose_name='Product Group', max_length=255)
    product_line = models.CharField(verbose_name='Product Line', max_length=255)
    product_description = models.CharField(verbose_name='Product Description', max_length=255)
    cost_category = models.CharField(verbose_name='Cost Category', max_length=255)

class VendorList(models.Model):
    vendor_code = models.CharField(verbose_name='Vendor Code', max_length=45, primary_key=True)
    vendor_name = models.CharField(verbose_name='Vendor Name', max_length=255)

class ShipmentData(models.Model):
    buying_office = models.CharField(verbose_name='Buying Office', max_length=45)
    sub_buying_office = models.CharField(verbose_name='Sub Buying Office', max_length=45)
    operating_company = models.CharField(verbose_name='Operating Company', max_length=45)
    vendor_code = models.ForeignKey(VendorList, on_delete=models.CASCADE)
    fin_month = models.DateTimeField(verbose_name='FinMonth')
    order_no = models.CharField(verbose_name='Order No', max_length=45)
    product_code = models.ForeignKey(ProductMaster, on_delete=models.CASCADE)
    order_quantity = models.FloatField(verbose_name='Order Quantity', default = 0)
    order_creation_date = models.DateTimeField(verbose_name='Order Creation Date')
    request_order_receiving_date = models.DateTimeField(verbose_name='Reqyest Order Receiving Date')
    official_order_receiving_date = models.DateTimeField(verbose_name='Official Order Receiving Date')
    actual_customer_request_date = models.DateTimeField(verbose_name='Actual Customer Request Date', default = timezone.now)
    actual_order_receiving_date = models.DateTimeField(verbose_name='Actual Order Receiving Date')
    order_official_date = models.DateTimeField(verbose_name='Order Official Date')
    payment_terms = models.CharField(verbose_name='Payment Terms', max_length=45)
    fob = models.FloatField(verbose_name='FoB', default = 0)
    shipment_value = models.FloatField(verbose_name='Shipment Value', default = 0)
    sku_order_index = models.CharField(verbose_name='SKU Order Index', max_length=45)
    vendor_moq = models.IntegerField(verbose_name='Vendor MOQ', default = 0)
    shipment_value_sku_order = models.FloatField(verbose_name='Shipment Value SKU Order', default = 0)
    moq_multiple = models.FloatField(verbose_name='MOQ Multiple', default = 0)
    year = models.IntegerField(verbose_name='Year', default = 0)
    moq_category_index = models.IntegerField(verbose_name='MOQ Category Index', default = 0)
    moq_category = models.CharField(verbose_name='MOQ Category', max_length=45)

class FixedCost(models.Model):
    vendor_code = models.ForeignKey(VendorList, on_delete=models.CASCADE)
    fixed_cost_percentage = models.FloatField(verbose_name='Fixed Cost %', default = 0)

class MOQCategory(models.Model):
    moq_category_index = models.IntegerField(verbose_name='MOQ Category Index', default = 0)
    moq_category = models.CharField(verbose_name='MOQ Category', max_length=45)
    moq_savings = models.FloatField(verbose_name='MOQ Efficiency Savings', default = 0)

class ShipmentCalc(models.Model):
    buying_office = models.CharField(verbose_name='Buying Office', max_length=45)
    category = models.CharField(verbose_name='Category', max_length=255)
    vendor_code = models.CharField(verbose_name='Vendor Code', max_length=45, default='')
    vendor_name = models.CharField(verbose_name='Vendor Name', max_length=255)
    fin_month = models.DateTimeField(verbose_name='FinMonth', default=0)
    year = models.IntegerField(verbose_name='Year', default = 0)
    sum_shipment_value = models.FloatField(verbose_name='Shipment Value', default = 0)
    sum_order_quantity = models.FloatField(verbose_name='Order Quantity', default = 0)
    avg_fob = models.FloatField(verbose_name='Average FoB', default = 0)
    avg_shipment_value_sku = models.FloatField(verbose_name='Average Shipment Value per SKU', default = 0)
    avg_order_quantity_sku = models.FloatField(verbose_name='Average Order Quantity per SKU', default = 0)
    avg_shipment_value_po = models.FloatField(verbose_name='Average Shipment Value per PO', default = 0)
    avg_order_quantity_po = models.FloatField(verbose_name='Average Order Quantity per PO', default = 0)
    num_sku = models.IntegerField(verbose_name='Number of Distinct SKU', default = 0)
    num_po = models.IntegerField(verbose_name='Number of Distinct PO', default = 0)
    sum_shipment_value_prior = models.FloatField(verbose_name='Prior Year Shipment Value', default = 0)
    shipment_growth = models.FloatField(verbose_name='Shipment Growth (%)', default = 0)
    growth_factor = models.FloatField(verbose_name='Growth Factor (%)', default = 0)
    TSP_ValueGrowth = models.FloatField(verbose_name='Theoretical Saving Potential - Value Growth', default = 0)
    TSP_MOQ = models.FloatField(verbose_name='Theoretical Saving Potential - MOQ', default = 0)
    TSP_CostPriceRecovery = models.FloatField(verbose_name='Theoretical Saving Potential - Cost Recovery', default = 0)
    TSP_MOT = models.FloatField(verbose_name='Theoretical Saving Potential - Money On the Table', default = 0)
    avg_cost_price = models.FloatField(verbose_name='Average cost price', default = 0)
    avg_cost_price_prior = models.FloatField(verbose_name='Prior Average cost price', default = 0)
    fixed_cost_percentage = models.FloatField(verbose_name='Fixed Cost %', default = 0)
    sum_shipment_value_sku_order = models.FloatField(verbose_name='Shipment Value SKU Order', default = 0)
    sum_vendor_moq = models.IntegerField(verbose_name='Vendor MOQ', default = 0)
    moq_multiple = models.FloatField(verbose_name='MOQ Multiple', default = 0)
    moq_category_index = models.IntegerField(verbose_name='MOQ Category Index', default = 0)
    moq_category = models.CharField(verbose_name='MOQ Category', max_length=45, default='')

class LaborRate(models.Model):
    provinces_with_factories = models.CharField(verbose_name='Provinces with Factories', max_length=255)
    pct_total_workers_for_vietnam = models.FloatField(verbose_name='Percent Total Workers for Vietnam', default = 0)
    min_wage_2015 = models.FloatField(verbose_name='2015 Min Wage', default = 0)
    min_wage_2016 = models.FloatField(verbose_name='2016 Min Wage', default = 0)
    total_premium = models.FloatField(verbose_name='Total Premium', default = 0)
    total_wage_LLC = models.FloatField(verbose_name='Total Wage (LLC)', default = 0)
    total_wage_USD = models.FloatField(verbose_name='Total Wage (USD)', default = 0)
    
class SourceLocationCalc(models.Model):
    # optional table
    buying_office = models.CharField(verbose_name='Buying Office', max_length=45)
    vendor_name = models.CharField(verbose_name='Vendor Name', max_length=255)
    vendor_code = models.CharField(verbose_name='Vendor Code', max_length=45)
    product_country_of_origin = models.CharField(verbose_name='Country of Origin', max_length=45)

    



# CostApp is only for costing analysis section. It is not used for vendor, entity level and money on the table sections.

class CostAppCommodity(models.Model):
    material = models.CharField(verbose_name='Material', max_length=45, primary_key=True)
    change = models.FloatField(verbose_name = 'Change', default = 0)

class CostAppComp(models.Model):
    product_type = models.CharField(verbose_name='Product Type', max_length=45)
    final_cost = models.FloatField(verbose_name = 'Final Cost', default = 0)
	
class CostAppCost(models.Model):
    product_code = models.CharField(verbose_name='Product Code', max_length=45, primary_key=True)
    product_name = models.CharField(verbose_name='Product Name', max_length=255)
    product_type = models.CharField(verbose_name='Product Type', max_length=45)
    standard_minutes = models.IntegerField(verbose_name='Standard Minutes', default = 0)
    raw_material = models.ForeignKey(CostAppCommodity, on_delete=models.CASCADE)
    material_cost = models.FloatField(verbose_name = 'Raw Material Cost', default = 0)	
    wastage_allowance = models.FloatField(verbose_name = 'Wastage Allowance', default = 0)
    overhead = models.FloatField(verbose_name = 'Overhead ($)', default = 0)

class CostAppWage(models.Model):
    country_of_origin = models.CharField(verbose_name = 'Country of Origin', max_length=45, primary_key=True)
    wage_rate = models.FloatField(verbose_name = 'Wage Rate ($/hour)', default = 0)

class CostAppVendor(models.Model):
    vendor_name = models.CharField(verbose_name='Vendor Name', max_length=255, primary_key=True)
    country_of_origin = models.CharField(verbose_name = 'Country of Origin', max_length=45)
    efficiency_adjustment = models.FloatField(verbose_name = 'Efficiency Adjustment', default = 0)

class CostAppDuty(models.Model):
    country_of_origin = models.CharField(verbose_name = 'Country of Origin', max_length=45)
    country_of_destination = models.CharField(verbose_name='Country of Destination', max_length=255)
    material = models.CharField(verbose_name='Material', max_length=45)
    duty_rate = models.FloatField(verbose_name = 'Duty Rate', default = 0)
    transportation = models.FloatField(verbose_name = 'Transportation', default = 0)
	
class GDP(models.Model):
	country = models.CharField(max_length =30)
	Year = models.IntegerField()
	Rate = models.DecimalField(max_digits=13, decimal_places=10)
	
class CPI(models.Model):
	country = models.CharField(max_length =30)
	Year = models.IntegerField()
	Rate = models.DecimalField(max_digits=13, decimal_places=10)

class Wage(models.Model):
	country = models.CharField(max_length =30)
	Year = models.IntegerField()
	Rate = models.DecimalField(max_digits=13, decimal_places=10)
	
class LaborOverview(models.Model):
	country = models.CharField(max_length =30)
	Provinces = models.CharField(max_length =30)
	Percentage = models.DecimalField(max_digits=13, decimal_places=10)
	MinWage2015 = models.DecimalField(max_digits=13, decimal_places=2)
	MinWage2016 = models.DecimalField(max_digits=13, decimal_places=2)
	Premium = models.DecimalField(max_digits=13, decimal_places=10)
	WageLLC = models.DecimalField(max_digits=13, decimal_places=2)
	WageUSD = models.DecimalField(max_digits=13, decimal_places=2)
	
class CurrencyMonthly(models.Model):
	country = models.CharField(max_length =30)
	Date = models.DateField()
	Rate = models.DecimalField(max_digits=13, decimal_places=2)
	Days = models.IntegerField()
	
class CurrencyYearly(models.Model):
	country = models.CharField(max_length =30)
	Status = models.CharField(max_length =30)
	Year = models.IntegerField()
	Rate = models.DecimalField(max_digits=13, decimal_places=10)	


