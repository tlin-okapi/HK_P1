/*******************************************************
Set up Side Panel Filters
Note that this code is shared among all pages that 
require a side panel filter.
********************************************************/

function setupFilter(ndx, selectedFilters){
	// Selected filters are specified in view.py.
	// This function will add the relevant filters into html

	var knownFilters_id = ['Analysis Period', 'Sourcing Office', 'Category', 'Vendor', 'Vendor Code', 'MOT Component'];
	var knownFilters_label = ['Analysis Period', 'Sourcing Office', 'Category', 'Vendor', 'Vendor', 'MOT Component'];
	var knownFilters_chart = ['chart-analysis-period', 'select-source-office', 'select-category', 'select-vendor', 'select-vendor', 'mot-table-filter'];

	if (selectedFilters.length > 0) {
		
		var scriptAdd = d3.select("#selectFilter");
		scriptAdd.append('h1').text('Filter');
		var fixedWidth = 200;

			// loop through known filter in sequence and add selected filters
		for (var iFilter=0; iFilter<knownFilters_id.length; iFilter++) {
			var filterID = knownFilters_id[iFilter];
			if (selectedFilters.indexOf(filterID) >= 0) {
			
				// add relevant div in the html
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
							.width(fixedWidth)
							.dimension(sourceOfficeDim) 
							.group(sourceOfficeDim.group()) 
							.title(function (d) {return d.key;} )
							.on('renderlet', function(chart) {
								chart.select("select.dc-select-menu").attr('style', 'width: ' + fixedWidth + 'px !important; min-width: ' + fixedWidth + 'px; max-width: ' + fixedWidth + 'px;');
								})
							; 
						break;

					case 'Category':
						// Category
						var categorySelect = dc.selectMenu("#select-category");
						chartStr = 'categorySelect';
						chartObj = categorySelect;
						var categoryDim = ndx.dimension(function(d) {return d.fields.category;});
						categorySelect 
							.width(fixedWidth)
							.dimension(categoryDim) 
							.group(categoryDim.group()) 
							.multiple(true)
							.numberVisible(5)
							.title(function (d) {return d.key;} )
							.on('renderlet', function(chart) {
								chart.select("select.dc-select-menu").attr('style', 'width: ' + fixedWidth + 'px !important; min-width: ' + fixedWidth + 'px; max-width: ' + fixedWidth + 'px;');
								})
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
							.width(fixedWidth)
							.dimension(vendorDim) 
							.group(vendorDim.group()) 
							.multiple(true)
							.numberVisible(12)
							.title(function (d) {return d.key;} )
							.on('renderlet', function(chart) {
								chart.select("select.dc-select-menu").attr('style', 'width: ' + fixedWidth + 'px !important; min-width: ' + fixedWidth + 'px; max-width: ' + fixedWidth + 'px;');
								})
							; 
						break;
						
					case 'MOT Component':
						var compList_id = ['mot-table-valuegrowth', 'mot-table-moq', 'mot-table-cpr', 'mot-table-leadtime', 'mot-table-margin'];
						var compList_label = ['Value Growth', 'MOQ', 'Cost Price Recovery', 'Lead Time', 'Margin'];
						for (var iComp=0; iComp<compList_id.length; iComp++) {
							var textField = d3.select("#" + compList_id[iComp]);
							var showChecked = (textField.attr("style") == "display: table-row;");
							var htmlStr = '<input type="checkbox" class="mot-comp-cb" value="' + compList_id[iComp] + '"';
							if (showChecked) {
								htmlStr = htmlStr + 'checked="' + showChecked + '"';
							}
							htmlStr = htmlStr + '>&nbsp;' + compList_label[iComp] + '&emsp;</input>';
							scriptAdd_div
								.append('tr')
								.html(htmlStr)								
							;
						}
						d3.selectAll(".mot-comp-cb").on('change', function() {
									if (this.checked) {
										d3.select("#" + this.value).attr("style", "display: table-row;");
										d3.select("#" + this.value + "-blank").attr("style", "display: none;");
									}
									else {
										d3.select("#" + this.value).attr("style", "display: none;");
										d3.select("#" + this.value + "-blank").attr("style", "display: table-row;");
									} 
								});
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

function snap_to_zero(aValue) {
	// when crossfilter adds or subtract large numbers with small ones, the end result isn't precise.
	return (Math.abs(aValue)<1e-4) ? 0 : aValue
}

function snap_to_zero_percent(aValue) {
	// when crossfilter adds or subtract large numbers with small ones, the end result isn't precise.
	return (Math.abs(aValue)<1e-6) ? 0 : aValue
}
