let quoteCtrl = require('./../controllers/quotes.js');


module.exports = function(app){
    // Root Request
	app.get('/', quoteCtrl.index);
	app.get('/show', quoteCtrl.show);
	app.post('/add', quoteCtrl.create);
}  