'use strict'

app.controller('rootCtrl', ['$rootScope', '$location', '$window', function($rootScope, $location, $window) {
    /** Root Controller **/
    $rootScope.go = function(path) {
        console.log(path);
        $location.path(path);
    };

    $rootScope.go_back = function() {
        $window.history.back();
    };

    $rootScope.set_active = function(key) {
        $rootScope.active_page = key;
    };
}]);

app.controller('homeCtrl', ['$scope', 'api-service', function($scope, api) {
    /** Home Controller **/
    $scope.submit = function() {
        $scope.msg = api.hello.query({name: $scope.name})
    };
}]);

app.controller('aboutCtrl', ['$scope', function($scope) {
    /** About Controller **/
    $scope.StringConst = '[[ Angular_Variable ]]'
}]);

