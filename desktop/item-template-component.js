angular.
module('item').
component('item', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: 'item-template.html',
  controller: function ExampleListController($http) {
            var self = this;
            $http.get('/data?_collection=items&name=iphone 5').then(function(response) {
                self.list = response.data;
            });
        }
});