var data = [{ "date": 2011, "pv": 0.05}, { "date": 2012, "pv": 0.07 }, { "date": 2013, "pv": 0.06 }, { "date": 2014, "pv": 0.04 }]

var dataTwo = [{ "date": 2011, "pv": 0.02 }, { "date": 2012, "pv": 0.02 }, { "date": 2013, "pv": 0.02 }, { "date": 2014, "pv": 0.02 }]

var dataThree = [{ "date": 2011, "pv": 0.07 }, { "date": 2012, "pv": 0.08 }, { "date": 2013, "pv": 0.07 }, { "date": 2014, "pv": 0.07 }]

CreateLines(data, dataTwo, dataThree);

function CreateLines(data, dataTwo, dataThree) {
    var dataset = [];
    var lines = [];//保存折线图对象
    var lineNames = [];//保存系列名称
    var lineColor = ["#BDC3C7", "#CB4335", "#34495E"];
    var currentLineNum = 0;
    var maxdata;//y轴最大值
	var formatPercent = d3.format(".0%");
    var margin = { top: 100, right: 20, bottom: 30, left: 40 },
        width = 1000,
        height = 300;
	var colorLegend = d3.scale.ordinal().range(["#5278a5", "#6ec6e2", "#5aa335", "#89c540", "#eae200", "#ffca2c", "#f7951e", "#a1a1a1"]),
		legendData = ["A","B","C","D","E","FG"];	
	var defaultPageLoad = true;
    var svg = d3.select("#main_body").append("svg")
				.attr("width", width)
				.attr("height", height + margin.top + margin.bottom)
				.append("g");	

	/* Set background */
    svg.append("rect").attr("class", "annual-yield-grid-background").attr({"height": height-10, "width": width, "x": 0, "y":margin.top/2+10});
	
	/* Chart title */
      svg.append("text")
      .attr("class", "title")
      .attr("x", 0).attr("y", margin.top/3).attr("text-anchor", "left")  
      .style({"font-size":"18px", "fill":"#7d7d7d","font-weight":"bold"}) 
      .text("Forecasted Wage Rate");
	
	/* Legend: Grades */
    colorLegend.domain(legendData);
    svg.append("text").attr({"x": 700, "y": margin.top/3}).text("Country").style({"fill":"#a1a1a1", "font-family": "Arial","font-size":"16px"});  

	var legend = svg.selectAll(".legend")
					.data(colorLegend.domain().slice())
					.enter()
					.append("g")
					.attr("class", "legend-grade")
					.attr("id", function(d, i) { return  "grade-" + d;})
					.attr("transform", function(d, i) { 
						var grades = legendData.length;
						return "translate(-" + (((grades - i) * 31) - 29) + ","+ margin.top/6 +")"; }
					);
					
	legend.append("rect")
		.attr("x", width - 52)
		.attr({"width": 26,"height": 26})
		.attr("class", function(d) { return "rect-grade-" + d; })
		.style({"fill": colorLegend, "cursor":"pointer"});
	
	legend.append("text")
		.attr("x", width - 39)
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

	/* should be dynamic*/
	function loadChartData(dataset){
		currentLineNum = dataset.length;
		maxdata = getMaxData(dataset);
		mindata = getMinData(dataset);
		console.log(maxdata,mindata);
		var xScale = d3.scale.ordinal()
			.domain((data.map(function (d) { return d.date; })))
			.rangeBands([0, width-100], 0, 0);

		var yScale = d3.scale.linear()
		.domain([0, maxdata])
		.range([height - margin.top - margin.bottom, 0]);
		
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
			.attr("transform", "translate(" + margin.left + "," + (height - margin.bottom) + ")")
			.call(xAxis)
			.append('text')
			//.text("Year")
			.attr("class", "xAxis")
			.attr('transform', 'translate(' + (width - margin.left - margin.right - 10) + ', -10)');

		svg.append("g")
			.attr("class", "axis")
			.attr("transform", "translate(" + (margin.left) + "," + margin.top + ")")
			.call(yAxis)
			.append('text')
			//.text("Rate")
			.attr("class", "yAxis");
			
		//addlegend();
		
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
        dataset.push(data);
        dataset.push(dataTwo);
        dataset.push(dataThree);
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
            .attr("y", 0)
            .attr("fill", function (d, i) { return lineColor[i]; });

        legend.selectAll("rect")
            .data(lineNames)
            .enter()
            .append("rect")
            .attr("x", function (d, i) { return i * 100 - 20; })
            .attr("y", -10)
            .attr("width", 12)
            .attr("height", 12)
            .attr("fill", function (d, i) { return lineColor[i]; });
        legend.attr("transform", "translate(" + ((width - lineNames.length * 100) / 2) + "," + (height + 10) + ")");
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
	/*
		d3.select("#annualYieldsChart").selectAll(".legend-grade").classed("selected", false);
		d3.select("#annualYieldsChart").selectAll(".legend-grade").selectAll("circle").remove();

		d3.select("#annualYieldsChart").select(".year-legend-label").remove();
		d3.select("#annualYieldsChart").selectAll(".legend-year").remove();
		d3.select("#annualYieldsChart").selectAll(".vintage").remove();
		d3.select("#annualYieldsChart").selectAll(".tick").remove();
		d3.select("#annualYieldsChart").selectAll("line").remove();
		d3.select("#annualYieldsChart").selectAll(".hline").remove();*/
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
		var selectedGrade = d3.select(this).text();
		var selectedDataSource = "data_" + selectedGrade;
		data = [{ "date": 2011, "pv": 0.03}, { "date": 2012, "pv": 0.07 }, { "date": 2013, "pv": 0.05 }, { "date": 2014, "pv": 0.04 }];
		dataTwo = [{ "date": 2011, "pv": 0.02 }, { "date": 2012, "pv": 0.02 }, { "date": 2013, "pv": 0.07 }, { "date": 2014, "pv": 0.02 }];
		dataThree = [{ "date": 2011, "pv": 0.01 }, { "date": 2012, "pv": 0.08 }, { "date": 2013, "pv": 0.01 }, { "date": 2014, "pv": 0.07 }];
		getData();
		console.log(dataset);
		loadChartData(dataset);
	});
}

