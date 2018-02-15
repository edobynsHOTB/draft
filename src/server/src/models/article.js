//article model here
'use strict';
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var articleModel = new Schema({
        createdAt: Date,
        createdBy: Schema.Types.ObjectId,
        agency: Schema.Types.ObjectId,
        role: Number,
        status: Number,
        title: String,
        summary: String,
        approvedBy: Schema.Types.ObjectId,
        tags: [String],
        views: Number,
        description: [{role: Number, value: String}],
        attachments: [{role: Number, value: [String]}]
    }, {
        collection: 'articles'
    });

module.exports = mongoose.model('article', articleModel);