
var app = angular.module("claimPredictApp", []);
app.controller("claimCtrl", function ($scope, $http) {

    $http.get(apiURL + "service/claim").then(function (response) {
        google.charts.load('current', { packages: ['corechart', 'line'] });
        google.charts.setOnLoadCallback(drawBasic);
        function drawBasic() {
            let data_arr =[];
            resp = response.data.data.forEach(function(element) {
                data_arr.push([Number(element.Actual),Number(element.Predicted)]);
            }, this);
            console.log(data_arr);
            var data = new google.visualization.DataTable();
            data.addColumn('number', 'Predicted');
            data.addColumn('number', 'Actual');

            data.addRows(data_arr);

            var options = {
                hAxis: {
                    title: 'Predicted'
                },
                vAxis: {
                    title: 'Actual'
                }
            };

            var chart = new google.visualization.LineChart(document.getElementById('probdist'));

            chart.draw(data, options);
        }
    });


});