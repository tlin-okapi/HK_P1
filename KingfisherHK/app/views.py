"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

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
            'message':'Strategic Decisions Group HQ',
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
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/entityLevel.html',
        {
            'title':'Main Dashboard - Entity Level',
            'year':datetime.now().year,
        }
    )


def mainDashboardVendorLevel(request):
    """Renders the main dashboard page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/vendorLevel.html',
        {
            'title':'Main Dashboard - Vendor Level',
            'year':datetime.now().year,
        }
    )

def valueGrowth(request):
    """Renders the Value Growth page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/valueGrowth.html',
        {
            'title':'Value Growth',
            'year':datetime.now().year,
        }
    )

def moq(request):
    """Renders the MOQ page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/moq.html',
        {
            'title':'MOQ',
            'year':datetime.now().year,
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
    """Renders the Margin page."""
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

def methodology(request):
    """Renders the Margin page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/methodology.html',
        {
            'title':'Methodology',
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