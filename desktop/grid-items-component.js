angular.
module('grid').
component('grid', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: 'grid-items-template.html',
  controller: function ExampleListController($http) {
            var self = this;
            $http.get('/data?_collection=items').then(function(response) {
                self.list = response.data;
            });
        }
});