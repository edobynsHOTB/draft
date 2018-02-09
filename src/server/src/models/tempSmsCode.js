'use strict';
var mongoose = require('mongoose');
var Schema = mongoose.Schema;


var tempSmsCode = new Schema({

        phone: {
            type: String
        },
        smsCode: {
            type: String
        }
}, {
        collection: 'tempSmsCode'
    });

module.exports = mongoose.model('tempSmsCode', tempSmsCode);