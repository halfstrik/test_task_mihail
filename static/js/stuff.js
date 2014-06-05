/*global $,ko,window*/
var SHOP = SHOP || {};
SHOP.stuff = SHOP.stuff || (function () {
    'use strict';
    $(function () {
        var stuffViewModel;
        stuffViewModel = {
            stuffs: ko.observableArray(),
            updateStuff: function () {
                $.getJSON('/goods/stuff' + window.location.search, function (json_data) {
                    var i;
                    stuffViewModel.stuffs.removeAll();
                    for (i = 0; i < json_data.length; i += 1) {
                        stuffViewModel.stuffs.push(json_data[i]);
                    }
                });
            },
            amount: ko.observable('All'),
            property_value: ko.observable(),
            property_value_options: ko.observableArray(),
            updateOptions: function () {
                $.getJSON('/goods/properties', function (json_data) {
                    var i;
                    stuffViewModel.property_value_options.removeAll();
                    for (i = 0; i < json_data.length; i += 1) {
                        stuffViewModel.property_value_options.push(json_data[i]);
                    }
                });
            },
            updateSelect: function () {
                var params = {};
                if (stuffViewModel.amount() !== 'All') {
                    params.amount = stuffViewModel.amount();
                }
                if (this.property_value() !== undefined) {
                    params.property_value = stuffViewModel.property_value();
                }
                window.history.pushState(null, 'Change parameters', '/?' + $.param(params));
                this.updateStuff();
            }
        };
        ko.applyBindings(stuffViewModel);
        stuffViewModel.updateStuff();
        stuffViewModel.updateOptions();
    });
}());
