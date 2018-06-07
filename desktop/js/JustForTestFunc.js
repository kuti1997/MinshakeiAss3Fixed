function justForTest($http, name) {
    var self = this;
    $http.get('/data?_collection=items&name=' + name).then(function (response) {
        self.list = response.data;
    });
}