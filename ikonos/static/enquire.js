'use strict';

var app = angular.module("Enquire", []); 

app.controller('EnquiryController', function($scope, $log, $http, $timeout) {
    $scope.submitButtonText = 'Submit';
    $scope.loading = false;
    $scope.submitEnquiry = function() {
        // get the URL from the input
        var data = {
            "email": $scope.email,
            "first_name": $scope.firstName,
            "last_name": $scope.lastName,
            "message": $scope.message
        }

        // fire the API request
        $http.post('/enquire', data).
            then(function(response) {
                getEnquiry(response.data);
                $scope.enquiryDetails = null;
                $scope.loading = true;
                $scope.submitButtonText = 'Loading...';
            }, function(response) {
                $log.log(response);
            });

        function getEnquiry(jobID) {
            var timeout = "";

            var poller = function() {
                // fire another request
                $http.get('/enquiry/'+jobID).
                    then(function(response) {
                        if(response.status === 202) {
                            $log.log(response.data, response.status);
                        } else if (response.status === 200){
                            $log.log(response.data);
                            $scope.loading = false;
                            $scope.submitButtonText = "Submit";
                            $scope.enquiryDetails = response.data;
                            $timeout.cancel(timeout);
                            return false;
                        }
                        // continue to call the poller() function every 2 seconds
                        // until the timeout is cancelled
                        timeout = $timeout(poller, 2000);
                    }, function(response) {
                        $log.log(response);
                    });
            };
            poller();
        }
    }
});