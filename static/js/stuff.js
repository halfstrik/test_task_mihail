/*global $,ko,window*/
var SHOP = SHOP || {};
SHOP.stuff = SHOP.stuff || (function () {
    'use strict';
    $(function () {
        var stuffViewModel;
        stuffViewModel = {
            stuffs: ko.observableArray(),
            update: function () {
                $.getJSON('/goods/stuff' + window.location.search, function (json_data) {
                    var i;
                    stuffViewModel.stuffs.removeAll();
                    for (i = 0; i < json_data.length; i += 1) {
                        stuffViewModel.stuffs.push(json_data[i]);
                    }
                });
            }
        };
        ko.applyBindings(stuffViewModel);
        stuffViewModel.update();
    });
}());
