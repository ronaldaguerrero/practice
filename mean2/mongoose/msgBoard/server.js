// Require the Express Module
var express = require('express');
// Create an Express App
var app = express();
// Require body-parser (to receive post data from clients)
var bodyParser = require('body-parser');
// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));
// Require path
var path = require('path');
// Require mongoose
var mongoose = require('mongoose');

// This is how we connect to the mongodb database using mongoose -- "basic_mongoose" is the name of
//   our db in mongodb -- this should match the name of the db you are going to use for your project.
mongoose.connect('mongodb://localhost/MessageDash');

var CommentSchema = new mongoose.Schema({
 name: String,
 comment: String,
}, {timestamps: true });

mongoose.model('Comment', CommentSchema); // We are setting this Schema in our Models as 'User'
var Comment = mongoose.model('Comment') // We are retrieving this Schema from our Models, named 'User'

var MessageSchema = new mongoose.Schema({
 name: String,
 message: String,
 comments: [CommentSchema]
}, {timestamps: true });

mongoose.model('Message', MessageSchema); // We are setting this Schema in our Models as 'User'
var Message = mongoose.model('Message') // We are retrieving this Schema from our Models, named 'User'

// Use native promises (only necessary with mongoose versions <= 4)
mongoose.Promise = global.Promise;

// Setting our Static Folder Directory
app.use(express.static(path.join(__dirname, './static')));
// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS
app.set('view engine', 'ejs');
// Routes
// Root Request


require('./server/config/routes.js')(app)



// Setting our Server to Listen on Port: 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
})
