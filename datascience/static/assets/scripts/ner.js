var app = angular.module("nerApp", []);
app.controller("postCtrl", function ($scope, $http) 
{
   $scope.submit = function (isValid) {
        if (isValid) 
        {
            $http.post("ner/", this.NER).then(function (result) 
            {
                $scope.summary = result.data;
            });
        }
   }
});

$(document).ready(function () 
{
    divolte.signal("ner",{});
});