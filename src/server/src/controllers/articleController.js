'use strict';

var mongoose = require('mongoose'),
    agency = mongoose.model('article');

//GET
exports.search = function (req, res) {
    var keyword = req.query.keyword;
    //var role = req.query.role;  
    res.send("result");
};    