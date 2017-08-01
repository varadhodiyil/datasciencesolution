var app = angular.module("langdetectApp", []);
app.controller("postCtrl", function ($scope, $http) 
{
   $scope.submit = function (isValid) {
        if (isValid) 
        {
            $http.post("#", this.LangDetect).then(function (result) 
            {
                $scope.summary = result.data;
            });
        }
   }
});

$(document).ready(function () {
    divolte.signal("LangDetect",{});
});
