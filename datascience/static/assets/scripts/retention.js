$(document).on('click', '.browse', function () {
    var file = $(this).parent().parent().parent().find('.file');
    file.trigger('click');
});
$(document).on('change', '.file', function () {
    $(this).parent().find('.form-control').val($(this).val().replace(/C:\\fakepath\\/i, ''));
});
var app = angular.module("clvApp", []);
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
        console.log(file);
        $http({
            url: uploadUrl,
            method: "POST",
            data: file,
            headers: { 'Content-Type': file.type }
        }).then(function (res) {
            console.log("Posted");
        }, function (fail) {
            console.log("Failed");
            console.log(fail);
        });
    }
}]);
app.controller("postCtrl", function ($scope, $http, fileUpload) {
    // $scope.CLV = {};
    // $scope.uploadFile = function () {
    //     var file = $scope.myFile;
    //     if (file == undefined || file.size == 0) {
    //         alert("Please Select a file");
    //     }
    //     else {
    //         // console.log('file is ');
    //         // console.dir(file);
    //         // var uploadUrl = apiURL + "service/churn";
    //         // var f = file;
    //         // r = new FileReader();
    //         // r.onloadend = function (e) {
    //         //     var data = e.target.result;
    //         //     //send your binary data via $http or $resource or do anything else with it
    //         //     fileUpload.uploadFileToUrl(data, uploadUrl);
    //         // }

    //         // r.readAsBinaryString(f);
    //     var reader = new FileReader();
    //     reader.readAsDataURL(file);
    //     reader.onload = function () 
    // 	{
    //         data =reader.result;
    //         d = {};
    //         d['file'] = data;
    //         d = JSON.stringify(d);
    //         console.log(d);
    //         $http.post(apiURL + "service/churn",d).then(
    //             function(result)
    //             {
    //                 console.log(result);
    //             });
    //     };

    //     }
    // };
    $scope.Retention = {};
    $scope.submit = function (isValid) {
        if (isValid) {
            $http.post(apiURL + "service/churn", this.Retention).then(function (result) {
                $scope.summary = result.data;
                chart_Data = result.data.data.graph1;
                google.charts.load("current", { packages: ['corechart'] });
                  google.charts.setOnLoadCallback(function() { drawChart(chart_Data); });
                function drawChart(d) {
                    // var data = google.visualization.arrayToDataTable([
                    //     ["Element", "Density", { role: "style" }],
                    // ]);
                    dataTable = new google.visualization.DataTable();
                    // dataTable.addRow(["Copper", 8.94, "#b87333"]); 
                    dataTable.addColumn('string', 'Feature');  
                    dataTable.addColumn('number', 'Importance'); 
                    d.forEach(function(element) {
                        dataTable.addRow([element.Featurename, (parseFloat(element.Importance).toFixed(2)*100  )]);
                        // console.log
                    }, this);

                    var options = {
                        title: "Percentage of Importance",
                        width: 502,
                        height: 320,
                        bar: { groupWidth: "55%" },
                        legend: { position: "none" },
                    };
                    var chart = new google.visualization.ColumnChart(document.getElementById("probdist"));
                    chart.draw(dataTable, options);
                }
            });
        }
    }
});