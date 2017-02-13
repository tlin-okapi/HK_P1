/*******************************************************
Set up Side Panel Filters
Note that this code is shared among all pages that 
require a side panel filter.
********************************************************/

function setupFilter(ndx, selectedFilters){
	// Selected filters are specified in view.py.
	// This function will add the relevant filters into html

	var knownFilters_id = ['Analysis Period', 'Sourcing Office', 'Category', 'Vendor', 'Vendor Code'];
	var knownFilters_label = ['Analysis Period', 'Sourcing Office', 'Category', 'Vendor', 'Vendor'];
	var knownFilters_chart = ['chart-analysis-period', 'select-source-office', 'select-category', 'select-vendor', 'select-vendor'];

	// loop through known filter in sequence and add selected filters
	for (var iFilter=0; iFilter<knownFilters_id.length; iFilter++) {
		var filterID = knownFilters_id[iFilter];
		if (selectedFilters.indexOf(filterID) >= 0) {
		
			// add relevant div in the html
			var scriptAdd = d3.select("#selectFilter")
			var scriptAdd_div = scriptAdd.append('div');
			scriptAdd_div
				.attr('id', knownFilters_chart[iFilter])
				.append('h5')
				.text(knownFilters_label[iFilter])
				;
			
			// add a break so that new element always appear in the next row
			// otherwise, multiple elements might float together in the same row
			scriptAdd
				.append('div')
				.attr('class', 'clearfix')
				;
			
			
			// connect the chart object
			var chartStr = '';
			var chartObj = '';
			switch (filterID) {
				case 'Analysis Period':
					// Analysis Period
					var yearRingChart = dc.pieChart("#chart-analysis-period");
					chartStr = 'yearRingChart';
					chartObj = yearRingChart;
					var yearDim = ndx.dimension(function(d) {return d.fields.year;});
					var year_total = yearDim.group().reduceSum(function(d) {return d.fields.sum_shipment_value;});
					yearRingChart
						.width(100)
						.height(100)
						.dimension(yearDim)
						.group(year_total)
						.innerRadius(10)
						;
					break;

				case 'Sourcing Office':
					// Sourcing Office
					var sourceOfficeSelect = dc.selectMenu("#select-source-office");
					chartStr = 'sourceOfficeSelect';
					chartObj = sourceOfficeSelect;
					var sourceOfficeDim = ndx.dimension(function(d) {return d.fields.buying_office;});
					sourceOfficeSelect 
						.width(200)
						.dimension(sourceOfficeDim) 
						.group(sourceOfficeDim.group()) 
						.title(function (d) {return d.key;} )
						; 
					break;

				case 'Category':
					// Category
					var categorySelect = dc.selectMenu("#select-category");
					chartStr = 'categorySelect';
					chartObj = categorySelect;
					var categoryDim = ndx.dimension(function(d) {return d.fields.category;});
					categorySelect 
						.width(200)
						.dimension(categoryDim) 
						.group(categoryDim.group()) 
						.multiple(true)
						.numberVisible(5)
						.title(function (d) {return d.key;} )
						; 
					break;

				case 'Vendor':
				case 'Vendor Code':
				case 'Vendor Code ID':
					// Vendor
					var vendorSelect = dc.selectMenu("#select-vendor");
					chartStr = 'vendorSelect';
					chartObj = vendorSelect;
					var vendorDim;
					if (filterID == 'Vendor')
							vendorDim = ndx.dimension(function(d) {return d.fields.vendor_name;});
					else if (filterID == 'Vendor Code')
							vendorDim = ndx.dimension(function(d) {return d.fields.vendor_code;});
					else if (filterID == 'Vendor Code ID')					
							vendorDim = ndx.dimension(function(d) {return d.fields.vendor_code_id;});

					vendorSelect 
						.width(200)
						.dimension(vendorDim) 
						.group(vendorDim.group()) 
						.multiple(true)
						.numberVisible(12)
						.title(function (d) {return d.key;} )
						; 
					break;

				default:
					break;
			}

/*			
			// add a reset status
			if (chartStr != '') {
				chartObj.controlsUseVisibility(true);
				scriptAdd_div
					.append('a')
					.attr('class', 'reset')
					.attr('href', 'javascript:' + chartStr + '.filterAll();dc.redrawAll();')
					.attr('style', 'visibility: hidden;')
					.text('reset')
					;
			}
*/


		}
	}

} // end of .setupFilter


function fixYAxisLabelOverlap(aChart, axisIndictor) {
	// y-axis label seems to be off on the charts because they run into the tick labels. 
	// This is temporary solution till CSS is fixed.
	var defaultPadding = 15;
	
	if (axisIndictor == 'left')
		aChart.margins().left = aChart.margins().left + defaultPadding;
	else
		aChart.margins().right = aChart.margins().right + defaultPadding;
	
}