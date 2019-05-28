let taskCtrl = require('./../controllers/taskCtrl.js');

module.exports = function(app){
	app.get('/tasks', taskCtrl.index);
	app.get('/tasks/:id', taskCtrl.show);
	app.post('/tasks', taskCtrl.create);
	app.put('/tasks/:id', taskCtrl.update);
	app.delete('/:id', taskCtrl.delete);
}

