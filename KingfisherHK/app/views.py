"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.core import serializers
from .models import *
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'SDG - Cost Analysis Platform',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Strategic Decisions Group HK',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Breaking down the barriers to good decisions',
            'year':datetime.now().year,
        }
    )

def mainDashboardEntityLevel(request):
    """Renders the main dashboard page."""
    shipments = ShipmentCalc.objects.all()
    
    data_json = serializers.serialize('json', 
        shipments, 
       fields=('buying_office', 
                'category',
                'vendor_code',
                'year',
                'sum_shipment_value',
                'TSP_ValueGrowth',
                'TSP_MOQ',
                'TSP_CostPriceRecovery',
                'TSP_MOT'))    
				
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/entityLevel.html',
        {
            'title':'Main Dashboard - Entity Level',
            'year':datetime.now().year,
            'data': data_json,
			'filters': ['Analysis Period', 'Sourcing Office', 'Category', 'Vendor Code'],
        }
    )


def mainDashboardVendorLevel(request):
    """Renders the main dashboard page."""
    shipments = ShipmentCalc.objects.all()
    
    data_json = serializers.serialize('json', 
        shipments, 
       fields=('buying_office', 
                'category',
                'vendor_code',
                'year',
                'sum_shipment_value',
                'sum_order_quantity',
				'num_sku',
				'num_po',
				'avg_cost_price',
                'TSP_ValueGrowth',
                'TSP_MOQ',
                'TSP_CostPriceRecovery',
                'TSP_MOT'))    
				
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/vendorLevel.html',
        {
            'title':'Main Dashboard - Vendor Level',
            'year':datetime.now().year,
            'data': data_json,
			'filters': ['Analysis Period', 'Sourcing Office', 'Category', 'Vendor Code', 'MOT Component'],
        }
    )

def valueGrowth(request):
    """Renders the Value Growth page."""
    shipments = ShipmentCalc.objects.all()
    
    data_json = serializers.serialize('json', 
        shipments, 
        fields=('buying_office', 
                'category',
                'vendor_code',
                'year',
                'sum_shipment_value',
                'sum_shipment_value_prior',
                'TSP_ValueGrowth',
                'fixed_cost_percentage'))    

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/valueGrowth.html',
        {
            'title':'Money on the Table Analysis - Value Growth',
            'year':datetime.now().year,
            'data': data_json,
			'filters': ['Analysis Period', 'Sourcing Office', 'Category', 'Vendor Code'],
        }
    )
    
	
def moq(request):
    """Renders the MOQ page."""
    shipments = ShipmentCalc.objects.all()
    
    data_json = serializers.serialize('json', 
        shipments, 
       fields=('buying_office', 
                'category',
                'vendor_code',
                'year',
                'sum_shipment_value',
                'sum_order_quantity',
                'TSP_MOQ',
                'moq_category',
                'moq_category_index'))    
	
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/moq.html',
        {
            'title':'Money on the Table Analysis - MOQ',
            'year':datetime.now().year,
            'data': data_json,
			'filters': ['Analysis Period', 'Sourcing Office', 'Category', 'Vendor Code'],
        }
    )

def leadTime(request):
    """Renders the Lead Time page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/leadTime.html',
        {
            'title':'Lead Time',
            'year':datetime.now().year,
        }
    )

def margin(request):
    """Renders the Margin page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/margin.html',
        {
            'title':'Margin',
            'year':datetime.now().year,
        }
    )

def methodology(request):
    """Renders the Methodology page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/methodology.html',
        {
            'title':'Methodology',
            'year':datetime.now().year,
        }
    )

def costInputNav(request):
	"""Renders the Margin page."""
	assert isinstance(request, HttpRequest)
	website=request.GET['level']
	return render(
		request,
		website,
		{
			'title':'Cost Input',
			'year':datetime.now().year,
		}
	)

def costInput(request):
    """Renders the Margin page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/costInput.html',
        {
            'title':'Cost Input',
            'year':datetime.now().year,
        }
    )	
	

def costOutput(request):
	product_code_input = request.GET['product_code']
	vendor_name_input = request.GET['vendor_name']
	country_origin_input = request.GET['country_origin']
	material_input = request.GET['material']
	country_destination_input = request.GET['country_destination']
	size = request.GET['size']
	currency = request.GET['currency']
	minute_linked = 0.005
	bom_linked=0.05
	
	Table_cost = CostAppCost.objects.get(product_code=product_code_input)
	cost_dict = model_to_dict(Table_cost,fields=['product_name', 'product_type','standard_minutes','wastage_allowance','overhead','material_cost','raw_material'])
	#Table_commodity = CostAppCommodity.objects.get(material=str(cost_dict['raw_material']))
	#commodity_dict = model_to_dict(Table_commodity, fields=['change'])
	
	Table_wage = CostAppWage.objects.get(country_of_origin=country_origin_input)
	wage_dict=model_to_dict(Table_wage,fields=['wage_rate'])
	Table_vendor = CostAppVendor.objects.get(vendor_name=vendor_name_input)
	vendor_dict=model_to_dict(Table_vendor,fields=['efficiency_adjustment'])
	Table_duty = CostAppDuty.objects.get(country_of_origin=country_origin_input,country_of_destination=country_destination_input,material=material_input)
	duty_dict=model_to_dict(Table_duty,fields=['transportation','duty_rate'])
	
	labor_payout=float(cost_dict['standard_minutes'])*float(wage_dict['wage_rate'])*float(vendor_dict['efficiency_adjustment'])
	#bom_cost=float(cost_dict['material_cost'])*float(cost_dict['wastage_allowance'])*float(commodity_dict['change'])
	bom_cost=float(cost_dict['material_cost'])+float(cost_dict['wastage_allowance'])	
	margin = float(minute_linked)*float(cost_dict['standard_minutes'])+float(bom_linked)*float(bom_cost)
	duty = float(duty_dict['duty_rate'])*(float(labor_payout)+float(bom_cost)+float(cost_dict['overhead'])+float(margin))
	fob=float(labor_payout)+float(bom_cost)+float(cost_dict['overhead'])+float(margin)
	final_cost=float(labor_payout)+float(bom_cost)+float(cost_dict['overhead'])+float(margin)+float(duty_dict['transportation'])+float(duty)
	
	return HttpResponse(json.dumps({'cost_approach':'Level III',
									'minute_linked':minute_linked,
									'bom_linked':bom_linked,
									'product_name':cost_dict['product_name'],
									'product_type':cost_dict['product_type'],
									'standard_minutes':cost_dict['standard_minutes'],
									'wastage_allowance': cost_dict['wastage_allowance'],
									'overhead':cost_dict['overhead'],
									'material_cost':cost_dict['material_cost'],
									#'commodity_change':commodity_dict['change'],
									'wage_rate':wage_dict['wage_rate'],
									'efficiency_adjustment':vendor_dict['efficiency_adjustment'],
									'transportation':duty_dict['transportation'],
									'duty_rate':duty_dict['duty_rate'],
									'labor_payout':labor_payout,
									'bom_cost':bom_cost,
									'margin':margin,
									'duty':duty,
									'fob':fob,
									'final_cost':final_cost}),content_type='application/json')
	
def costPriceEvolution(request):
    """Renders the Margin page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/costPriceEvolution.html',
        {
            'title':'Cost Price Evolution',
            'year':datetime.now().year,
        }
    )

def commodityData(request):
    """Renders the Margin page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/commodityData.html',
        {
            'title':'Commodity Data',
            'year':datetime.now().year,
        }
    )

# Navigate to Labor Rate Page
def laborRate(request):
    """Renders the Margin page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/laborRate.html',
        {
            'title':'Labor Rate',
            'year':datetime.now().year,
        }
    )
	
# Load Data for Labor Rate Table and Chart	
def laborRateChart(request):
	countrySelected = request.GET['country']	
	# Retrive data for wage table
	Table_result = LaborOverview.objects.filter(country=countrySelected)
	Table_serial = [{"Provinces with factories":o.Provinces,"% of Total workers":str("{:.1%}".format(o.Percentage)),"2015 Min Wage": str(o.MinWage2015), "2016 Min Wage": str(o.MinWage2016), "Total Premium": str("{:.1%}".format(o.Premium)), "Total Wage (LLC)": str(o.WageLLC), "Total Wage (USD)": str(o.WageUSD) } for o in Table_result];
	# Retrive data for wage chart
	GDP_result = GDP.objects.filter(country=countrySelected)
	GDP_serial = [{'date':o.Year,'pv':str(o.Rate)} for o in GDP_result]	
	CPI_result = CPI.objects.filter(country=countrySelected)
	CPI_serial = [{'date':o.Year,'pv':str(o.Rate)} for o in CPI_result]	
	Wage_result = Wage.objects.filter(country=countrySelected)
	Wage_serial = [{'date':o.Year,'pv':str(o.Rate)} for o in Wage_result]	
	return HttpResponse(json.dumps({'Table':Table_serial,'GDP':GDP_serial,'CPI':CPI_serial,'Wage':Wage_serial}), content_type='application/json')

	
def currency(request):
    """Renders the Margin page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/currency.html',
        {
            'title':'Currency',
            'year':datetime.now().year,
        }
    )

def currencyChart(request):
	countrySelected = request.GET['country']	
	# Retrive data for monthly currency table
	Table_result = CurrencyMonthly.objects.filter(country=countrySelected).order_by('-id')[:10]
	Table_result = reversed(Table_result)
	Table_serial = [{"Year":o.Date.year,"Month":o.Date.month,"Monthly Average": str(o.Rate), "Days": str(o.Days) } for o in Table_result];
	Year_result = list(CurrencyYearly.objects.filter(country=countrySelected).values('Year').distinct())
	
	
	# Retrive data for wage chart
	Actual_result = CurrencyYearly.objects.filter(country=countrySelected,Status="Actual").order_by('Year')
	Actual_serial = [{'date':o.Year,'pv':str(o.Rate)} for o in Actual_result]	
	Projected_result = CurrencyYearly.objects.filter(country=countrySelected,Status="Projected").order_by('Year')
	Projected_serial = [{'date':o.Year,'pv':str(o.Rate)} for o in Projected_result]	
	Calculated_result = CurrencyYearly.objects.filter(country=countrySelected,Status="Calculated").order_by('Year')
	Calculated_serial = [{'date':o.Year,'pv':str(o.Rate)} for o in Calculated_result]	
	return HttpResponse(json.dumps({'Table':Table_serial,'Actual':Actual_serial,'Projected':Projected_serial,'Calculated':Calculated_serial,'Year':Year_result}), content_type='application/json')

def inflation(request):
    """Renders the Margin page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/inflation.html',
        {
            'title':'Inflation',
            'year':datetime.now().year,
        }
    )

def dutyScenario(request):
    """Renders the Margin page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/dutyScenario.html',
        {
            'title':'Duty Scenario',
            'year':datetime.now().year,
        }
    )

def standardProcess(request):
    """Renders the Margin page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/standardProcess.html',
        {
            'title':'Standard Process',
            'year':datetime.now().year,
        }
    )
