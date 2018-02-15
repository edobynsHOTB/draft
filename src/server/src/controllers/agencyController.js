'use strict';

var mongoose = require('mongoose'),
    agency = mongoose.model('agency');

//GET /agencies
exports.getAgencies = function (req, res) {
    var returnlist = [];
    var query = agency.find(); 
    query.exec(function (err, agencies) {
        if (err) return handleError(err);
        agencies.forEach(function(ag, index) {
            var obj = {};
            obj['name'] = ag.value;
            obj['articleCount'] = index;
            returnlist.push(obj); 
        })
        res.json(returnlist); 
    });
};    