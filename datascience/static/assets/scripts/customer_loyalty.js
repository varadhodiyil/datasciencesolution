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
    $scope.CLV = {};
    $scope.uploadFile = function () {
        var file = $scope.myFile;
        if (file == undefined || file.size == 0) {
            alert("Please Select a file");
        }
        else {
            console.log('file is ');
            console.dir(file);
            var uploadUrl = apiURL + "service/loyalty";
            fileUpload.uploadFileToUrl(file, uploadUrl);
            $(document).ready(function () 
            {
                divolte.signal("customerLoyalty_Submit",{});
            });
        }
    };
});


$(document).ready(function () 
{
    divolte.signal("customerLoyalty",{});
});