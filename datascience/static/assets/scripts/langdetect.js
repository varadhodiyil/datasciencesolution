var app = angular.module("langdetectApp", []);
app.controller("postCtrl", function ($scope, $http) 
{
   $scope.submit = function (isValid) {
        if (isValid) 
        {
            $(document).ready(function () 
            {
                    divolte.signal("Lang_Detect_Submit",{"queryString":this.LangDetect});
            });
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
