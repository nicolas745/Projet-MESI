const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);
let page = require("./serv/index")
new page(app)

io.on('connection', (socket) => {
  console.log('a user connected');
});

server.listen(80, () => {
  console.log('listening on *:80');
});