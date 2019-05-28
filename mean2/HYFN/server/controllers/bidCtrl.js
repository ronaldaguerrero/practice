let mongoose = require('mongoose');
let Task = mongoose.model('tasks');

module.exports = {
	index: function (req, res) {
		Task.find({}, function(err, tasks){
			if (err) {
				res.json(err);
	        } else {
	            res.json({tasks});
	        }
		})
	},

	show: function (req, res){
		Task.find({_id: req.params.id}, function (err, task){
			if (err) {
				res.json(err);
	        } else {
	            res.json({task});
	        }
		})
	},

	create: function (req, res) {
		Task.create(req.body, function (err, task){
			if (err) {
				res.json(err);
	        } else {
	            res.json({task});
	        }
		})
	},

	update: function (req, res) {
		Task.updateOne({_id: req.params.id}, {$set: req.body}, function (err, task){
			if (err) {
				res.json(err);
	        } else {
	            res.json(task);
	        }
		})
	},

	delete: function (req, res) {
		Task.deleteOne({_id: req.params.id}, function (err, task){
			if (err) {
				res.json(err);
	        } else {
	            res.json(task);
	        }
		})
	}
}