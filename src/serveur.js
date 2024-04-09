const express = require('express');
const app = express();
const port = 8080;
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);
let page = require("./serv/index")
new page(app)
io.on('connection', (socket) => {
  console.log('a user connected');
});

server.listen(port, () => {
  console.log("listening on *:"+port);
});