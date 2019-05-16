let express = require('express');
let app = express();
let mongoose = require('mongoose');
let bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(express.static(__dirname + '/public/dist/public/'));

mongoose.connect("mongodb://localhost/taskApi", { useNewUrlParser: true });

// require('./server/config/mongoose.js');
// require('./server/config/routes.js')(app);

app.listen(8000, function() {
  console.log("Listening on port 8000")
})