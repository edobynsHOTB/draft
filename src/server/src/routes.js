'use strict';

module.exports = function (app) {
//***********CONTROLLERS****************************//
    var tagsController = require('./controllers/tagsController');
    var agencyController = require('./controllers/agencyController');
    var articleController = require('./controllers/articleController');


//***********ROUTES****************************//

var prefix = '/api/v1'; 

//tagRoutes
    //GET    
        app.route(prefix + '/tags').get(tagsController.getTags);

    //POST

    //PUT

    //DELETE

//agencyRoutes
    //GET
        app.route(prefix + '/agencies').get(agencyController.getAgencies);
    
    //POST

    //PUT

    //DELETE

//articleRoutes
    //GET
        app.route(prefix + '/search').get(articleController.search);
        //app.route('/api/v1/articles').get(articleController.getArticles);
    //POST

    //PUT

    //DELETE
};