'''
This file is our Node.js server. It handles incoming connections and broadcasts drawing data to all connected clients.
'''
var io = require('socket.io')(process.env.PORT || 3000);
io.on('connection', function(socket) {
    socket.on('draw', function(data) {
        socket.broadcast.emit('draw', data);
    });
});