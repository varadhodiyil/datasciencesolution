var app = angular.module("summarizerApp", []);
app.controller("postCtrl", function ($scope, $http) 
{
   $scope.submit = function (isValid) {
        if (isValid) 
        {
            $(document).ready(function () {
                divolte.signal("Summarizer_Submit",{"queryString":this.Summarize});
            });
            $http.post("summarize/", this.Summarize).then(function (result) 
            {
                $scope.summary = result.data;
            });
        }
   }
});

$(document).ready(function () {
    divolte.signal("Summarizer",{});
});
