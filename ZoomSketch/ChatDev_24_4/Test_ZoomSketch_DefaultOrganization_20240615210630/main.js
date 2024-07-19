'''
This file contains the main JavaScript code for handling user interactions and communicating with the server.
'''
var canvas = document.getElementById('drawingCanvas');
var context = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var drawing = false;
var socket = io();
canvas.addEventListener('mousedown', function(e) {
    drawing = true;
    draw(e.pageX - canvas.offsetLeft, e.pageY - canvas.offsetTop, false);
});
canvas.addEventListener('mousemove', function(e) {
    if (drawing) {
        draw(e.pageX - canvas.offsetLeft, e.pageY - canvas.offsetTop, true);
    }
});
canvas.addEventListener('mouseup', function() {
    drawing = false;
});
canvas.addEventListener('touchstart', function(e) {
    drawing = true;
    draw(e.touches[0].pageX - canvas.offsetLeft, e.touches[0].pageY - canvas.offsetTop, false);
});
canvas.addEventListener('touchmove', function(e) {
    if (drawing) {
        draw(e.touches[0].pageX - canvas.offsetLeft, e.touches[0].pageY - canvas.offsetTop, true);
    }
});
canvas.addEventListener('touchend', function() {
    drawing = false;
});
window.addEventListener('resize', function() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});
function draw(x, y, isDrawing, fromServer) {
    if (isDrawing) {
        context.lineTo(x, y);
        context.stroke();
    } else {
        context.beginPath();
        context.moveTo(x, y);
    }
    if (!fromServer) {
        socket.emit('draw', { x: x, y: y, drawing: isDrawing });
    }
}
socket.on('draw', function(data) {
    draw(data.x, data.y, data.drawing, true);
});