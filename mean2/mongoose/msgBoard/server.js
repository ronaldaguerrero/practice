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
app.get('/', function(req, res) {
    // This is where we will retrieve the users from the database and include them in the view page we will be rendering.
    Message.find({}, function(err, msgs){
      res.render('index', {msgs: msgs});
    })
})

// Add User Request 
app.post('/add', function(req, res) {
  console.log("POST DATA", req.body);
  // create a new User with the name and age corresponding to those from req.body
  var message = new Message({name: req.body.name, message: req.body.message});
  // Try to save that new user to the database (this is the method that actually inserts into the db) and run a callback function with an error (if any) from the operation.
  message.save(function(err) {
    // if there is an error console.log that something went wrong!
    if(err) {
      console.log('something went wrong');
    } else { // else console.log that we did well and then redirect to the root route
      console.log('successfully added a Message!');
    }
    res.redirect('/');
  })
})

// Add User Request 
app.post('/addC/:id', function(req, res) {
  console.log("POST DATA", req.body);
  // create a new User with the name and age corresponding to those from req.body
  // Try to save that new user to the database (this is the method that actually inserts into the db) and run a callback function with an error (if any) from the operation.
  Comment.create(req.body, function(err, data) {
    // if there is an error console.log that something went wrong!
    if(err) {
      console.log('something went wrong');
    } else { // else console.log that we did well and then redirect to the root route
      Message.findOneAndUpdate({_id: req.params.id}, {$push: {comments: data}}, function(err,data){
        if(err){
           console.log('something went wrong');
        } else {
          console.log('successfully added a Comment!');
        }
      })
    }
  })
  res.redirect('/');
})


app.get('/Message/destroy/:id', function(req,res){
    Message.remove({_id: req.params.id}, function(err){
        res.redirect('/');
    })
})




// Setting our Server to Listen on Port: 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
})
