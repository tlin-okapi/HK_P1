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
                'sum_vendor_moq',
                'TSP_ValueGrowth',
                'sum_vendor_moq'))    
				
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
                'sum_shipment_value_sku_order',
                'sum_vendor_moq',
				'num_sku',
				'num_po',
                'TSP_ValueGrowth',
                'sum_vendor_moq'))    
				
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/vendorLevel.html',
        {
            'title':'Main Dashboard - Vendor Level',
            'year':datetime.now().year,
            'data': data_json,
			'filters': ['Analysis Period', 'Sourcing Office', 'Category', 'Vendor Code'],
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
                'shipment_growth',
                'growth_factor',
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
                'sum_vendor_moq',
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