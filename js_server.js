// server.js
const WebSocket = require('ws');
const server = new WebSocket.Server({ port: 8081 });

let clients = [];

server.on('connection', (ws) => {
    console.log('New user connected');
    clients.push(ws);

    // Broadcast incoming messages to all other connected clients
    ws.on('message', (message) => {
        console.log('Received:', message.toString());
        clients.forEach((client) => {
            if (client !== ws && client.readyState === WebSocket.OPEN) {
                client.send(message);
            }
        });
    });

    // Handle client disconnection
    ws.on('close', () => {
        console.log('User disconnected');
        clients = clients.filter((client) => client !== ws);
    });
});

console.log('WebSocket server running on ws://localhost:8080');
