var contact_app = angular.module("contactApp", []);
contact_app.controller("contactCtrl", function ($scope, $http) {
    $scope.Contact = {};
    $scope.hasErrors = false;
    $scope.submit = function (isValid) {
        if (isValid) {
            $http.post("contact/", this.Contact).then(function (result) {
                // $(document).ready(function () {
                //     divolte.signal("contact", { "queryString": $scope.contact });
                // });
                if (result.data.status) {
                    $scope.hasErrors = true;
                    alert("Thank You for Contacting us. We'll be in touch with you soon");
                    window.location.reload();
                    return;
                }
                else{
                    $scope.hasErrors = true;
                    $scope.errors = result.data.error;
                }
                
            });
        }
    }
});
angular.bootstrap(document.getElementById("demorequest"), ['contactApp']);