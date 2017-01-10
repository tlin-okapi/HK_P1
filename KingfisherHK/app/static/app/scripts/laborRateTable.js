function tabulate(data, columns) {
    var table = d3.select("#main_body").append("table"),
    thead = table.append("thead"),
    tbody = table.append("tbody");

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

// create some data
var dataset = [{ "Provinces with factories": "BINH CHIEU WARD", "Total workers for Vietnam": "4.20%", "2015 Min Wage": "3,100,000", "2016 Min Wage": "3,500,000", "Total Premium": "63%", "Total Wage (LLC)": "5,705,000", "Total Wage (USD)": "251" },
{ "Provinces with factories": "BINH DUONG", "Total workers for Vietnam": "0.30%", "2015 Min Wage": "2,150,000", "2016 Min Wage": "2,400,000", "Total Premium": "63%", "Total Wage (LLC)": "3,912,000", "Total Wage (USD)": "172.1" },
{ "Provinces with factories": "DONG NAI", "Total workers for Vietnam": "51.60%", "2015 Min Wage": "3,100,000", "2016 Min Wage": "3,500,000", "Total Premium": "63%", "Total Wage (LLC)": "5,705,000", "Total Wage (USD)": "251" },
{ "Provinces with factories": "DONG THAP", "Total workers for Vietnam": "1.00%", "2015 Min Wage": "2,150,000", "2016 Min Wage": "2,400,000", "Total Premium": "63%", "Total Wage (LLC)": "3,912,000", "Total Wage (USD)": "172.1" },
{ "Provinces with factories": "LONG AN", "Total workers for Vietnam": "9.40%", "2015 Min Wage": "2,400,000", "2016 Min Wage": "2,700,000", "Total Premium": "63%", "Total Wage (LLC)": "4,401,000", "Total Wage (USD)": "193.6" },
{ "Provinces with factories": "NINH BINH", "Total workers for Vietnam": "2.90%", "2015 Min Wage": "2,750,000", "2016 Min Wage": "3,100,000", "Total Premium": "63%", "Total Wage (LLC)": "5,053,000", "Total Wage (USD)": "222.3" },
{ "Provinces with factories": "TAYNINH", "Total workers for Vietnam": "8.40%", "2015 Min Wage": "2,400,000", "2016 Min Wage": "2,700,000", "Total Premium": "63%", "Total Wage (LLC)": "4,401,000", "Total Wage (USD)": "193.6" },
{ "Provinces with factories": "THAN HOA", "Total workers for Vietnam": "3.90%", "2015 Min Wage": "2,150,000", "2016 Min Wage": "2,400,000", "Total Premium": "63%", "Total Wage (LLC)": "3,912,000", "Total Wage (USD)": "172.1" },
{ "Provinces with factories": "TIEN GIANG", "Total workers for Vietnam": "1.20%", "2015 Min Wage": "2,750,000", "2016 Min Wage": "3,100,000", "Total Premium": "63%", "Total Wage (LLC)": "5,053,000", "Total Wage (USD)": "222.3" },
{ "Provinces with factories": "HO CHI MINH", "Total workers for Vietnam": "7.80%", "2015 Min Wage": "3,100,000", "2016 Min Wage": "3,500,000", "Total Premium": "63%", "Total Wage (LLC)": "5,705,000", "Total Wage (USD)": "251" },
{ "Provinces with factories": "HAIPHONG", "Total workers for Vietnam": "3.00%", "2015 Min Wage": "3,100,000", "2016 Min Wage": "3,500,000", "Total Premium": "63%", "Total Wage (LLC)": "5,705,000", "Total Wage (USD)": "251" },
{ "Provinces with factories": "VINH LONG", "Total workers for Vietnam": "6.20%", "2015 Min Wage": "2,400,000", "2016 Min Wage": "2,700,000", "Total Premium": "63%", "Total Wage (LLC)": "4,401,000", "Total Wage (USD)": "193.6" }];

// render the table
var laborTable = tabulate(dataset, ["Provinces with factories", "Total workers for Vietnam", "2015 Min Wage", "2016 Min Wage", "Total Premium", "Total Wage (LLC)", "Total Wage (USD)"]);

// uppercase the column headers
laborTable.selectAll("thead th")
    .text(function (column) {
        return column.charAt(0).toUpperCase() + column.substr(1);
    });

//// sort by age
//peopleTable.selectAll("tbody tr")
//    .sort(function(a, b) {
//        return d3.descending(a.age, b.age);
//    });


//d3.select("#main_body").selectAll("div")
//    .data(dataset) // <-- The answer is here!
//    .enter()
//    .append("div")e
//    .attr("class", "bar")
//    .style("height", function (d) {
//        var barHeight = d * 5;            
//        return barHeight + "px";
//});
