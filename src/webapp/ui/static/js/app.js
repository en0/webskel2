var app = angular.module('myapp', ['ngRoute', 'ngResource','ui.bootstrap']);

app.config(['$routeProvider', '$interpolateProvider', function($routeProvider, $interpolateProvider) {
    $routeProvider
        .when("/", {templateUrl: "partials/home.html", controller: "homeCtrl"})
        .when("/home", {templateUrl: "partials/home.html", controller: "homeCtrl"})
        .when("/about", {templateUrl: "partials/about.html", controller: "aboutCtrl"})
        .when("/404", {templateUrl: "partials/404.html", controller: "nullCtrl", isPublic: true})
        .otherwise({ redirectTo: '/404' });

    $interpolateProvider
        .startSymbol('[[')
        .endSymbol(']]');
}]);

