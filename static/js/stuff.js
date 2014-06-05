/*global $,ko*/
var SHOP = SHOP || {};
SHOP.stuff = SHOP.stuff || (function () {
    'use strict';
    $(function () {
        var stuffViewModel;
        stuffViewModel = {
            stuffs: ko.observableArray()
        };
        ko.applyBindings(stuffViewModel);
        $.getJSON("/goods/stuff", function (json_data) {
            var i;
            stuffViewModel.stuffs.removeAll();
            for (i = 0; i < json_data.length; i += 1) {
                stuffViewModel.stuffs.push(json_data[i]);
            }
        });
    });
}());
