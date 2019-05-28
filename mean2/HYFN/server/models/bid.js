// model
const mongoose = require('mongoose');

const taskSchema = new mongoose.Schema({
	title: {type: String, required: true},
	desc: {type: String, default: ''},
	completed: {type: Boolean, default: false}
}, {timestamps:true});

const Task = mongoose.model('tasks', taskSchema);
