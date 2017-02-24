"""
Definition of urls for KingfisherHK.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^entityLevel', app.views.mainDashboardEntityLevel, name='mainDashboardEntityLevel'),
    url(r'^vendorLevel', app.views.mainDashboardVendorLevel, name='mainDashboardVendorLevel'),
    url(r'^valueGrowth', app.views.valueGrowth, name='valueGrowth'),
    url(r'^moq', app.views.moq, name='moq'),
    url(r'^leadTime', app.views.leadTime, name='leadTime'),
    url(r'^margin', app.views.margin, name='margin'),
    url(r'^methodology', app.views.methodology, name='methodology'),
	
    url(r'^costInput$', app.views.costInput, name='costInput'),
	url(r'^costInputNav$', app.views.costInputNav, name='costInputNav'),
	url(r'^costOutput', app.views.costOutput, name='costOutput'),
	url(r'^costChart$', app.views.costChart, name='costChart'),	
    
	url(r'^costPriceEvolution', app.views.costPriceEvolution, name='costPriceEvolution'),
    url(r'^commodityData', app.views.commodityData, name='commodityData'),
	url(r'^laborRate', app.views.laborRate, name='laborRate'),
	url(r'^labor_chart$', app.views.laborRateChart, name='laborRateChart'),
	url(r'^currency$', app.views.currency, name='currency'),
	url(r'^currency_chart$', app.views.currencyChart, name='currencyChart'),
	url(r'^inflation', app.views.inflation, name='inflation'),
    url(r'^dutyScenario', app.views.dutyScenario, name='dutyScenario'),
    url(r'^standardProcess', app.views.standardProcess, name='standardProcess'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
