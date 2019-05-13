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

var moment = require('moment');

// This is how we connect to the mongodb database using mongoose -- "basic_mongoose" is the name of
//   our db in mongodb -- this should match the name of the db you are going to use for your project.
mongoose.connect('mongodb://localhost/dogDashboard');

var DogSchema = new mongoose.Schema({
 name: String,
 breed: String
}, {timestamps: true });

mongoose.model('Dog', DogSchema); // We are setting this Schema in our Models as 'User'
var Dog = mongoose.model('Dog') // We are retrieving this Schema from our Models, named 'User'

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
    Dog.find({}, function(err, dogs){
      res.render('index', {dogs: dogs});
    })
})

app.get('/add', function(req, res) {
    // This is where we will retrieve the users from the database and include them in the view page we will be rendering.
      res.render('new');
})

// Add User Request 
app.post('/add', function(req, res) {
  console.log("POST DATA", req.body);
  // create a new User with the name and age corresponding to those from req.body
  var dog = new Dog({name: req.body.name, breed: req.body.breed});
  // Try to save that new user to the database (this is the method that actually inserts into the db) and run a callback function with an error (if any) from the operation.
  dog.save(function(err) {
    // if there is an error console.log that something went wrong!
    if(err) {
      console.log('something went wrong');
    } else { // else console.log that we did well and then redirect to the root route
      console.log('successfully added a dog!');
    }
    res.redirect('/');
  })
})

app.get('/dog/:id', function(req, res) {
    // This is where we will retrieve the quotes from the database and include them in the view page we will be rendering.
    Dog.findOne({_id: req.params.id}, function(err, dog){
      if(err) {console.log(err); }
      res.render('show', {dog: dog});
    })
})

app.get('/dog/edit/:id', function(req, res) {
    // This is where we will retrieve the quotes from the database and include them in the view page we will be rendering.
    Dog.findOne({_id: req.params.id}, function(err, dog){
      if(err) {console.log(err); }
      res.render('edit', {dog: dog});
    })
})

app.post('/update/:id', function(req, res) {
    console.log("POST DATA", req.body);
    Dog.update({_id: req.params.id},
      {name: req.body.name,
      breed: req.body.breed},
      function(err){
        if(err) {
            console.log('something went wrong');
            res.redirect(`/edit/${req.params.id}`)
        } else {
            res.redirect(`/`);
        }
    })
})

app.get('/dog/destroy/:id', function(req,res){
    Dog.remove({_id: req.params.id}, function(err){
        res.redirect('/');
    })
})




// Setting our Server to Listen on Port: 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
})
