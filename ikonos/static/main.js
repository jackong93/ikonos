(function () {
    'use strict';

    angular.module('IkonosApp', [])

    .controller('EnquiryController', ['$scope', '$log', '$http', '$timeout',
        function($scope, $log, $http, $timeout) {
            $scope.submitEnquiry = function() {
                $log.log("test");
                
                // get the URL from the input
                var data = {
                    "email": $scope.email,
                    "first_name": $scope.firstName,
                    "last_name": $scope.lastName,
                    "message": $scope.message
                }

                // fire the API request
                $http.post('/enquire', data).
                    success(function(results) {
                        getEnquiry(results);
                    }).
                    error(function(error) {
                        $log.log(error);
                    });
                };

                function getEnquiry(jobID) {
                    var timeout = "";

                    var poller = function() {
                        // fire another request
                        $http.get('/enquiry/'+jobID).
                        success(function(data, status, headers, config) {
                            if(status === 202) {
                                $log.log(data, status);
                            } else if (status === 200){
                                $log.log(data);
                                $scope.enquiryDetails = data;
                                $timeout.cancel(timeout);
                                return false;
                            }
                            // continue to call the poller() function every 2 seconds
                            // until the timeout is cancelled
                            timeout = $timeout(poller, 2000);
                        });
                    };
                    poller();
                }
        }
    ]);
}());