// Load the express module and store it in the variable express (Where do you think this comes from?)
var express = require("express");
// console.log("Let's find out what express is", express);
// invoke express and store the result in the variable app
var app = express();
// console.log("Let's find out what app is", app);
// use app's get method and pass it the base route '/' and a callback
// require body-parser
var bodyParser = require('body-parser');
// use it!

app.use(express.static(__dirname + "/public"));
const server = app.listen(1337);
const io = require('socket.io')(server);
var counter = 0;

app.use(bodyParser.urlencoded({extended: true}));

app.get('/', function(request, response) {
   response.render("index");
})



    
io.on('connection', function (socket) { //2
  let count = 0;
  socket.on('click', function (data) { //7
    console.log(data); //8 (note: this log will be on your server's terminal)
    if (count == 0){
			count++;
		}
		else {
			count++;
		}
    socket.emit('updated_count', {res: count});
  });

  socket.on('reset', function (){
  	count = 0;
  	socket.emit('updated_count', {res: count});
  });
});




// this is the line that tells our server to use the "/static" folder for static content
app.use(express.static(__dirname + "/static"));
// two underscores before dirname
// try printing out __dirname using console.log to see what it is and why we use it

// This sets the location where express will look for the ejs views
app.set('views', __dirname + '/views'); 
// Now lets set the view engine itself so that express knows that we are using ejs as opposed to another templating engine like jade
app.set('view engine', 'ejs');