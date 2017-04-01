var express = require('express')
  , bodyParser = require('body-parser');
var app = express();
var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('/var/www/html/apps/radiogit/db.sqlite');

app.get('/', function (req, res) {
    res.send('RadioGit backend is up and running')
})

app.use(bodyParser.json());
app.post('/test', function(request, response){
  //console.log(request.body);
  var text = request.body.repository.full_name + " - " + request.body.commits[0].author.username + " committed " + request.body.commits[0].message + " " + " " + request.body.commits[0].url;
  var query = 'INSERT INTO Payloads VALUES (NULL, "' + request.body.repository.full_name + '","' + text + '")';
  response.send("Thank you kind sir");
  db.serialize(function() {
    db.run(query);
    console.log(query);
  });

  
});

app.listen(3000);

process.on('SIGINT', function(){
  console.log('Cya');
  db.close();
  process.exit(0);
});