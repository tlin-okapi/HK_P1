﻿$(document).ready(function(){
	$.getJSON('/labor_chart',{'country':'CN'},function(ret){
		var GDP = ret['GDP'];
		var CPI = ret['CPI'];
		var Wage = ret['Wage'];
		var Table = ret['Table'];		
		CreateLines(GDP, CPI, Wage, Table);
	})
})

function CreateLines(GDP, CPI, Wage, Table) {
	var table = d3.select("#main_body").append("table"),
	thead = table.append("thead"),
	tbody = table.append("tbody");
	var laborTable = tabulate(Table, ["Provinces with factories", "% of Total workers", "2015 Min Wage", "2016 Min Wage", "Total Premium", "Total Wage (LLC)", "Total Wage (USD)"]);
	laborTable.selectAll("thead th")
			.text(function (column) {
						return column.charAt(0).toUpperCase() + column.substr(1);
					});
		
    var dataset = [];
    var lines = [];//保存折线图对象
    var lineNames = ["GDP","CPI","Min Wage"];//保存系列名称
    var lineColor = ["#BDC3C7", "#CB4335", "#34495E"];
    var currentLineNum = 0;
    var maxdata;//y轴最大值
	var formatPercent = d3.format(".0%");
    var margin = { top: 100, right: 20, bottom: 100, left: 40 },
        width = 1000,
        height = 300;
	var colorLegend = d3.scale.ordinal().range(["#5278a5", "#6ec6e2", "#5aa335", "#89c540", "#eae200", "#ffca2c", "#f7951e", "#a1a1a1"]),
		legendData = ["CN","VN","KH","ID","IN","TH","KR","LK"];	
	var defaultPageLoad = true;
    var svg = d3.select("#main_body").append("svg")
				.attr("width", width)
				.attr("height", height + margin.top + margin.bottom)
				.append("g");	

	/* Set background */
    svg.append("rect").attr("class", "annual-yield-grid-background").attr({"height": height-50, "width": width, "x": 0, "y":margin.top/2+10});
	
	/* Chart title */
      svg.append("text")
      .attr("class", "title")
      .attr("x", 0).attr("y", margin.top/3).attr("text-anchor", "left")  
      .style({"font-size":"18px", "fill":"#7d7d7d","font-weight":"bold"}) 
      .text("Forecasted Wage Rate");
	
	/* Legend: Grades */
    colorLegend.domain(legendData);
    svg.append("text").attr({"x": 0, "y": (height+40)}).text("Country:").style({"fill":"#a1a1a1", "font-family": "Arial","font-size":"16px"});  

	var legend = svg.selectAll(".legend")
					.data(colorLegend.domain().slice())
					.enter()
					.append("g")
					.attr("class", "legend-grade")
					.attr("id", function(d, i) { return  "grade-" + d;})
					.attr("transform", function(d, i) { 
						var grades = legendData.length;
						return "translate(-" + (((grades - i) * 51) +470) + ","+ (height + 20) +")"; }
					);
					
	legend.append("rect")
		.attr("x", width - 52)
		.attr({"width": 36,"height": 26})
		.attr("class", function(d) { return "rect-grade-" + d; })
		.style({"fill": colorLegend, "cursor":"pointer"});
	
	legend.append("text")
		.attr("x", width - 35)
		.attr("y", 14)
		.attr("dy", ".25em")
		.text(function(d,i) { return d; })
		.style({"fill": "#fff", "cursor": "pointer"})
		.attr("text-anchor", "middle") 
		.attr("font-weight", function(d, i){
			if (d === "All") { return ("normal"); } else { return ("bold"); }
		})
		.attr("text-transform", function(d, i){
			if (d === "All") { return ("none"); } else { return ("uppercase"); }
	});	
	
	
	/* Using for loop to draw multiple vertical lines */
	var drawVerticalGridLines = function(gridWidth){
		for (var j=gridWidth; j <= width; j=j+gridWidth) {
			svg.append("svg:line")
				.attr("class", "vertical-grid-lines")
				.attr("x1", j-gridWidth)
				.attr("y1", 0)
				.attr("x2", j-gridWidth)
				.attr("y2", height)
				.style("stroke", function(){
					return j%3===0 ? "#e4e4e4" : "#f8f8f8";
				})
				.style("stroke-width", 1.5);
			};
		};
	
	if (defaultPageLoad){
		getData();
		loadChartData(dataset);
		defaultPageLoad=false;
	}

	function tabulate(data, columns) {
		var cellH = 20;
		var cellW = 200;

		// append the header row
		thead.append("tr")
			.selectAll("th")
			.data(columns)
			.enter()
			.append("th")
				.text(function (column) { return column; });

		// create a row for each object in the data
		var rows = tbody.selectAll("tr")
			.data(data)
			.enter()
			.append("tr");

		// create a cell in each row for each column
		var cells = rows.selectAll("td")
			.data(function (row) {
				return columns.map(function (column) {
					return { column: column, value: row[column] };
				});
			})
			.enter()
			.append("td")
				.text(function (d) { return d.value; });

		return table;
	}	
	
	
	
	/* should be dynamic*/
	function loadChartData(dataset){
		currentLineNum = dataset.length;
		maxdata = getMaxData(dataset);
		mindata = getMinData(dataset);
		console.log(maxdata,mindata);
		var xScale = d3.scale.ordinal()
			.domain((GDP.map(function (d) { return d.date; })))
			.rangeBands([0, width-100], 0, 0);

		var yScale = d3.scale.linear()
		.domain([0, maxdata])
		.range([height - margin.top - 50, 0]);
		
		var xAxis = d3.svg.axis()
		.scale(xScale)
		.orient("bottom");
		
		var yAxis = d3.svg.axis()
		.scale(yScale)
		.orient("left")
		.ticks(3)
		.tickFormat(formatPercent);

		svg.append("g")
			.attr("class", "axis")
			.attr("transform", "translate(" + margin.left + "," + (height - 50) + ")")
			.call(xAxis)
			.append('text')
			//.text("Year")
			.attr("class", "xAxis")
			.attr('transform', 'translate(' + (width - margin.left - margin.right - 10) + ', -100)');

		svg.append("g")
			.attr("class", "axis")
			.attr("transform", "translate(" + (margin.left) + "," + 100+ ")")
			.call(yAxis)
			.append('text')
			//.text("Rate")
			.attr("class", "yAxis");
			
		addlegend();
		
		for (i = 0; i < currentLineNum; i++) {
			var newLine = new CreateLineObject();
			newLine.init(i);
			lines.push(newLine);
		}
		
		
		function CreateLineObject() {

			this.init = function (id) {

				var arr = dataset[id];
				var line = d3.svg.line()
				.x(function (d) { return xScale(d.date); })
				.y(function (d) { return yScale(d.pv); })
				.interpolate('cardinal');

				svg.append("path")
					.datum(arr)
					.attr("transform", "translate(" + (margin.left + xScale.rangeBand() / 2) + "," + margin.top + ")")
					.attr("class", "line")
					.transition()
					.ease("elastic")
					.duration(1000)
					.delay(function (d, j) {
						return 200 * j;
					})
					.style("stroke", lineColor[id])
					.attr("d", line);

				svg.append('g').selectAll('circle')
					.data(arr)
					.enter()
					.append('circle')
					.attr("class","datacircle")
					.on('mouseover', function (d) {
						d3.select(this).transition().duration(500).attr('r', 5);
						d3.select('.tips').style('display', 'block');
						var tx = parseFloat(d3.select(this).attr("cx"));
						var ty = parseFloat(d3.select(this).attr("cy"));
						var tipRectx = tx + 60 + 180 > width ? tx + 10 - 180 : tx + 60,
							tipRecty = ty + 20 + 60 > height ? ty + 10 - 60 : ty + 20;
						var theDate = d.date;
						var thePv = d.pv;
						var tips = svg.append("g")
						.attr("id", "tips");
						var tipRect = tips.append("rect")
						.attr("x", tipRectx)
						.attr("y", tipRecty)
						.attr("width", 180)
						.attr("height", 60)
						.attr("fill", "#FFF")
						.attr("stroke", "#CCC")
						var tipText = tips.append("text")
						.attr("class", "tiptools")
						.text("Year:" + theDate)
						.attr("x", tipRectx + 20)
						.attr("y", tipRecty + 20);
						var tipText = tips.append("text")
						.attr("class", "tiptools")
						.text("Rate: " + d3.format('%')(thePv))
						.attr("x", tipRectx + 20)
						.attr("y", tipRecty + 50);

					})
					.on('mouseout', function () {
						d3.select(this).transition().duration(500).attr('r', 3.5);
						d3.select('.tips').style('display', 'none');
						d3.select("#tips").remove();
					})
					.on("click", function (d) {
						alert("Year：" + d.date + "\r\n Rate：" + d3.format('%')(d.pv));
					})
					.transition()
					.ease("elastic")
					.duration(1000)
					.delay(function (d, j) {
						return 200 * j;
					})
					.attr("transform", "translate(" + (margin.left + xScale.rangeBand() / 2) + "," + margin.top + ")")
				   .attr('cy', line.y())
				   .attr('cx', line.x())
				   .attr('r', 3)
				   .attr("fill", lineColor[id]);
			}
		}
	}
	
    function getData() {
		dataset=[];
        dataset.push(GDP);
        dataset.push(CPI);
        dataset.push(Wage);
    }

    function getMaxData(arr) {
        var maxdata = 0;
        for (var i = 0; i < arr.length; i++) {
            maxdata = d3.max([maxdata, d3.max(arr[i], function (d) { return d.pv; })]);
        }
        return maxdata;
    }

    function getMinData(arr) {
        var mindata;
        for (var i = 0; i < arr.length; i++) {
            mindata = d3.min([mindata, d3.min(arr[i], function (d) { return d.pv; })]);
        }
        return mindata;
    }

    function addlegend() {
        var legend = svg.append('g');
        legend.selectAll("text")
            .data(lineNames)
            .enter()
            .append("text")
            .text(function (d) { return d; })
            .attr("class", "legend")
            .attr("x", function (d, i) { return i * 100; })
            .attr("y", 20)
            .attr("fill", function (d, i) { return lineColor[i]; });

        legend.selectAll("rect")
            .data(lineNames)
            .enter()
            .append("rect")
            .attr("x", function (d, i) { return i * 100 - 20; })
            .attr("y", 10)
            .attr("width", 12)
            .attr("height", 12)
			.attr("class", "legend")
            .attr("fill", function (d, i) { return lineColor[i]; });
        legend.attr("transform", "translate(" + ((width - lineNames.length * 100) / 2) + "," + (height -20) + ")");
    }
	
	/* Interaction: Grade selection - Only one grade is selected at a time */
	legend.on("click", function(e) {
		var selectedAnnualYieldGrade = d3.select(this).text(),
		xPos = +(d3.select(this).select("rect").attr("x")) + 14;
		d3.select("#main_body").selectAll(".legend-grade").selectAll("circle").remove();
		d3.select("#main_body").select("g.xAxis").remove();
		d3.select("#main_body").select("g.yAxis").remove();
		d3.select("#main_body").selectAll(".tick").remove();
		d3.select("#main_body").selectAll("path.line").remove();
		d3.select("#main_body").selectAll("circle.datacircle").remove();
		d3.select("#main_body").selectAll(".legend").remove();
		d3.select("#main_body").selectAll("table").selectAll("th").remove();
		d3.select("#main_body").selectAll("table").selectAll("tr").remove();
		

	/* Set the selected Grade & Term */
		d3.select(this).classed("selected", true);
		d3.select(this).select("text").classed("selected", true);
		d3.select(this).append("circle")
					.attr("cx", xPos).attr("cy", 33).attr("r", 3).attr("width", 3).attr("height", 3)
					.style("fill", function(){
						var selectedGradeId = "#grade-"+selectedAnnualYieldGrade,
						circleColour = d3.select("#main_body")
										.select(selectedGradeId)
										.select("rect").style("fill");
										return circleColour;
					});
		/* Get the selected Grade & Term */
		var selectedCountry = d3.select(this).text();
		var selectedDataSource = "data_" + selectedDataSource;
		
		$.getJSON('/labor_chart',{'country':selectedCountry},function(ret){
				GDP = ret['GDP'];
				CPI = ret['CPI'];
				Wage = ret['Wage'];
				Table = ret['Table'];
				console.log('Hi');
				laborTable = tabulate(Table, ["Provinces with factories", "% of Total workers", "2015 Min Wage", "2016 Min Wage", "Total Premium", "Total Wage (LLC)", "Total Wage (USD)"]);
				laborTable.selectAll("thead th")
						.text(function (column) {
								return column.charAt(0).toUpperCase() + column.substr(1);
							});
				getData();
				console.log(selectedCountry);
				loadChartData(dataset);
		});
	});
}

