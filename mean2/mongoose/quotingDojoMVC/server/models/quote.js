// model
const mongoose = require('mongoose');

var QuoteSchema = new mongoose.Schema({
 name: String,
 quote: String
}, {timestamps: true });

var Quote = mongoose.model('Quote', QuoteSchema) // We are retrieving this Schema from our Models, named 'User'