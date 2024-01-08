var http = require('http');
var express = require('express');
var socketIO = require('socket.io');

var app = express();
var server = http.createServer(app);
var io = socketIO(server);

// Set up Express routes
app.get('/', function (req, res) {
  res.sendFile(__dirname + 'src/index.html');
});

// Set up Socket.io events
io.on('connection', function (socket) {
  console.log('A user connected');

  socket.on('disconnect', function () {
    console.log('User disconnected');
  });
});

// Set up HTTP server
server.listen(80, function () {
  console.log('Server is listening on port 80');
});
