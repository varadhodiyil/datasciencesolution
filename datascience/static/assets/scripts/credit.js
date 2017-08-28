var app = angular.module("creditApp", []);

app.controller("postCtrl", function ($scope, $http) {
    $scope.Credit = {};
    $scope.submit = function (isValid) {
        if (isValid) {
            $(document).ready(function () 
            {
                    divolte.signal("CreditAnalysis_Submit",{"query":$scope.Credit});
            });
            $http.post(base+"/predit/", this.Credit).then(function (result) {
                google.charts.load("current", { packages: ['corechart'] });
                google.charts.setOnLoadCallback(drawChart);
                function drawChart() 
                {
                    var data = google.visualization.arrayToDataTable([
                        ["Class", "Probbalility", { role: "style" }],
                        [result.data.classes[0], result.data.probability[0], "#b87333"],
                        [result.data.classes[1], result.data.probability[1], "silver"],
                    ]);

                    var view = new google.visualization.DataView(data);
                    view.setColumns([0, 1,
                        {
                            calc: "stringify",
                            sourceColumn: 1,
                            type: "string",
                            role: "annotation"
                        },
                        2]);
                    let label ="";
                    if(result.data.predicted == "1")
                    {
                        label = " will default on loan";
                    }
                    if(result.data.predicted == "0")
                    {
                        label = " will  not default";
                    }
                    console.log(label);
                    var options = {
                        title: " Predicted : " + label,
                        width: 502,
                        height: 636,
                        bar: { groupWidth: "30%" },
                        legend: { position: "none" },
                    };
                    var chart = new google.visualization.ColumnChart(document.getElementById("probdist"));
                    chart.draw(view, options);
                }

            });
        }
        else {
            console.log("not valid");
        }
    };
    $scope.submit(true);
});
    $(document).ready(function () {
        divolte.signal("CreditAnalysis",{});
    });
