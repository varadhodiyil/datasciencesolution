var app = angular.module("sentimentApp", []);
app.controller("postCtrl", function ($scope, $http) 
{
   $scope.submit = function (isValid) {
        if (isValid) 
        {
            $http.post("summarize/", this.Sentment).then(function (result) 
            {
                $scope.summary = result.data;
            });
        }
   }
});

$(document).ready(function () {
    divolte.signal("SentimentAnalysis",{});
});
