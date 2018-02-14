'use strict';
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var tag = new Schema({
        value: {
            type: String
        }
    }, {
        collection: 'tags'
    });

module.exports = mongoose.model('tag', tag);