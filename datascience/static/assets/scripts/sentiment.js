var app = angular.module("sentimentApp", []);
app.controller("postCtrl", function ($scope, $http) 
{
   $scope.submit = function (isValid) {
        if (isValid) 
        {
            $(document).ready(function () {
                divolte.signal("SentimentAnalysis_Submit",{"queryString":this.Sentment});
            });
            $http.post(apiURL+"service/sentiment", this.Sentment).then(function (result) 
            {
                $scope.summary = result.data;
            });
        }
   }
});

$(document).ready(function () {
    divolte.signal("SentimentAnalysis",{});
});
