$(document).on('click', '.browse', function () {
    var file = $(this).parent().parent().parent().find('.file');
    file.trigger('click');
});
$(document).on('change', '.file', function () {
    $(this).parent().find('.form-control').val($(this).val().replace(/C:\\fakepath\\/i, ''));
});
var app = angular.module("loyaltyApp", []);
app.directive('fileModel', ['$parse', function ($parse) {
    return {
        restrict: 'A',
        link: function (scope, element, attrs) {
            var model = $parse(attrs.fileModel);
            var modelSetter = model.assign;

            element.bind('change', function () {
                scope.$apply(function () {
                    modelSetter(scope, element[0].files[0]);
                });
            });
        }
    };
}]);
app.service('fileUpload', ['$http', function ($http) {
    this.uploadFileToUrl = function (file, uploadUrl) {
        var fd = new FormData();
        fd.append('file', file);
        $http({
            url: uploadUrl,
            method: "POST",
            data: fd,
            headers: { 'Content-Type': undefined }
        }).then(function (res) {
            console.log("Posted");
        });
    }
}]);
app.controller("postCtrl", function ($scope, $http, fileUpload) {
    $scope.isLoaded = false;
    $scope.Loyalty = {};
    $scope.submit = function (isValid) {
        if (isValid) {
             $scope.isLoaded = true;
             $(document).ready(function () 
            {
                    divolte.signal("Customer_loyalty_Submit",{"queryString":this.Loyalty});
            });
            $http.post(apiURL + "service/loyalty", this.Loyalty).then(function (result) {
                $scope.summary = result.data;
                chart_Data = result.data.data;
                google.charts.load("current", { packages: ['corechart'] });
                  google.charts.setOnLoadCallback(function() { drawChart(chart_Data); });
                function drawChart(d) {
                    // var data = google.visualization.arrayToDataTable([
                    //     ["Element", "Density", { role: "style" }],
                    // ]);
                    dataTable_A = new google.visualization.DataTable();
                    dataTable_Q = new google.visualization.DataTable();
                    // dataTable.addRow(["Copper", 8.94, "#b87333"]); 
                    dataTable_A.addColumn('string', 'Month');  
                    dataTable_A.addColumn('number', 'Amount');
                    dataTable_Q.addColumn('string', 'Month');  
                    dataTable_Q.addColumn('number', 'Quantity');
                    d[0].forEach(function(element) 
                    {
                        if(element.Purchase == "Amount")
                        {
                            dataTable_A.addRow([element.Month, Number(parseFloat(element.Value).toFixed(2)  )]);    
                        }
                        if(element.Purchase == "Quantity")
                        {
                            dataTable_Q.addRow([element.Month, Number(parseFloat(element.Value).toFixed(2)  )]);    
                        }
                    }, this);

                    var options_1 = {
                        title: "Month Vs Sale Amount",
                        width: 502,
                        height: 320,
                        bar: { groupWidth: "55%" },
                        legend: { position: "none" },
                    };
                    var options_2 = {
                        title: "Month Vs Quantity",
                        width: 502,
                        height: 320,
                        bar: { groupWidth: "55%" },
                        legend: { position: "none" },
                    };
                    var chart_1 = new google.visualization.ColumnChart(document.getElementById("probdist_1"));
                    chart_1.draw(dataTable_A, options_1);
                    var chart_2 = new google.visualization.ColumnChart(document.getElementById("probdist_2"));
                    chart_2.draw(dataTable_Q, options_2);
                    
                }
            });
        }
    }
});


$(document).ready(function () 
{
    divolte.signal("customerLoyalty",{});
    $('#clv').DataTable(
        {
            // scrollX : true,
            searching: false
        }
    );
});
