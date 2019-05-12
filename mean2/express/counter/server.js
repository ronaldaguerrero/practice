// Load the express module and store it in the variable express (Where do you think this comes from?)
var express = require("express");
// console.log("Let's find out what express is", express);
// invoke express and store the result in the variable app
var app = express();
// console.log("Let's find out what app is", app);

// require body-parser
var bodyParser = require('body-parser');
// use it!
app.use(bodyParser.urlencoded({extended: true}));

// new code:
var session = require('express-session');

// more new code:
app.use(session({
  secret: 'keyboardsecret',
  resave: false,
  saveUninitialized: true,
  cookie: { maxAge: 60000 }
}))


app.get('/', function (req, res){
    // set the name property of session.  
    if(req.session.count == null){
      req.session.count = 1;  
    } else {
      req.session.count++;
    }
    let count = req.session.count;
    //code to add user to db goes here!
    // redirect the user back to the root route. 
    res.render('index', {count: count});
});

app.get('/add2', function (req, res){
    req.session.count+= 1;
    //code to add user to db goes here!
    // redirect the user back to the root route. 
    res.redirect('/');
});

app.get('/reset', function (req, res){
  req.session.count = 0;
  res.redirect('/');
})

// this is the line that tells our server to use the "/static" folder for static content
app.use(express.static(__dirname + "/static"));
// two underscores before dirname
// try printing out __dirname using console.log to see what it is and why we use it

// This sets the location where express will look for the ejs views
app.set('views', __dirname + '/views'); 
// Now lets set the view engine itself so that express knows that we are using ejs as opposed to another templating engine like jade
app.set('view engine', 'ejs');


// tell the express app to listen on port 8000, always put this at the end of your server.js file
app.listen(8000, function() {
  console.log("listening on port 8000");
})
