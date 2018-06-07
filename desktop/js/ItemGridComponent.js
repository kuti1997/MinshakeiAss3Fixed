angular.
module('itemInGrid').
component('itemInGrid', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: 'itemInGrid-template.html',
  controller: function ExampleListController($http) {
            var self = this;
            $http.get('/data?_collection=items').then(function(response) {
                self.list = response.data;
            });
        }
});