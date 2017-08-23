var app = angular.module("clickStreamApp", []);
app.controller("postCtrl", function ($scope, $http) {
    google.charts.load('current', { packages: ['corechart'] });
    $http.get(base+"/clickstream").then(function (response) {
        google.charts.setOnLoadCallback(drawChart_1);
        response = response.data;
        function drawChart_1() {
            var data = google.visualization.arrayToDataTable([
                ['Element', 'Density'],
                ['Total Visits', response.visits],
                ['Unique Visits', response.unique_visits],

            ]);
            var options = {
                title: "Visits ",
                width: 520,
                height: 620,
                bar: { groupWidth: "50%" },
                legend: { position: "none" },
            };
            var chart = new google.visualization.ColumnChart(document.getElementById('main_1'));
            chart.draw(data, options);
            dataTable = new google.visualization.DataTable();
            // dataTable.addRow(["Copper", 8.94, "#b87333"]); 
            dataTable.addColumn('string', 'Events');
            dataTable.addColumn('number', 'Count/Event');
            let d = response.distinctEvents;
            Object.keys(d).forEach(function (element) {
                dataTable.addRow([element, Number(d[element])]);
            }, this);
            console.log(dataTable);
            var options = {
                pieHole: 0.3,
                width: 502,
                height: 600,
                legend: { position: "none" },
            };
            var chart = new google.visualization.PieChart(document.getElementById("main_2"));
            chart.draw(dataTable, options);
        }

    });
});
$(document).ready(function () {
    divolte.signal("Clickstream",{});
});
