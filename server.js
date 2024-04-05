const express = require('express');
const app = express();
const port = 8080;
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);
let page = require("./serv/index")
app.use(express.static('mesi2024/build'))
new page(app)
io.on('connection', (socket) => {
  console.log('a user connected');
});

server.listen(port, () => {
  console.log("listening on *:"+port);
});
