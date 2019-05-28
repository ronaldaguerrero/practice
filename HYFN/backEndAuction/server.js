let express = require('express');
let app = express();
let mongoose = require('mongoose');
let bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');

mongoose.connect("mongodb://localhost/auction", { useNewUrlParser: true });

const itemSchema = new mongoose.Schema({
  name: {type: String, required: [true, "A name is required"], minlength: 3},
    listedPrice: {type: Number, required: [true, "A price is required"], minlength: 1},
    deadline: {type: Date},
    currentBid: {type: Number},
    currentBidder: {type: Number},
    soldPrice: {type: Number},
    winner: {type: String},
    }, {timestamps: true})

const userSchema = new mongoose.Schema({
  name: {type: String},
  points: {type: Number},
  items: [itemSchema]

}, {timestamps: true });

var Item = mongoose.model('items', itemSchema);
var User = mongoose.model('users', userSchema);

app.get('/', function (req, res) {
  Item.find({},(function(err, is) {
        if (err) res.render('/index', {errors: err});
        else {
            res.render('index', {is: is});
        }
    }))
});


app.post('/create_item', function (req, res) {
  Item.create(req.body, function (err, result) {
    if (err) { 
      console.log('we have an error');
        res.redirect('/');
    } else {
      res.redirect('/');
      }
    });
});

// create server and socket
const server = app.listen(1337);
var io = require('socket.io')(server);
var counter = 0;

io.on("connection", function(socket){
  console.log("Connected");
  socket.on("pageLoad", function(data){ // 3 receive name and run if else
      if(user_check(data.user) === true) {
        socket.emit("existingUser", {error: "This user already exits"})
      } else {
        users.push(data.user); // 4 push user to array
        socket.emit("loadMessages", {currentUser: data.user, messages: messages}) // 5 send user and messages to client
      }
    })

    socket.on("newMessage", function(data){
      messages.push({name: data.user, message: data.message}) // receive & push user and message from client to array
      io.emit("postNewMessage", {newMessage: data.message, user: data.user}) // send new message to client
    })
    

  })