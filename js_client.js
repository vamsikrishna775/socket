// client.js
const WebSocket = require('ws');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Connect to WebSocket server
const ws = new WebSocket('ws://localhost:8081');

ws.on('open', () => {
    console.log('Connected to the chat server');
    promptMessage();
});

ws.on('message', (message) => {
    console.log(`\nReceived: ${message}`);
    promptMessage();
});

ws.on('close', () => {
    console.log('Disconnected from the server');
    rl.close();
});

function promptMessage() {
    rl.question('Enter message: ', (msg) => {
        ws.send(msg);
        promptMessage();
    });
}
