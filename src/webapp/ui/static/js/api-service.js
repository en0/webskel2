'use strict'

var API_CONF = {
    "URL": "/api/v1"
};

angular.module('myapp')
.factory('api-service', ['$resource', function($resource) {
    var _hello = $resource(API_CONF.URL+"/hello/:name", {name: '@name'}, {
        query: { method: 'GET', isArray: false }
    });

    return {
        get hello() { return _hello; }
    };
}]);
