const WebSocket = require('ws');

// Replace the following line with your WebSocket server URL
const ws = new WebSocket('ws://example.com/');

ws.on('open', function() {
  console.log('Connected to WebSocket server.');
  ws.send('Hello Server!');
});

ws.on('message', function(data) {
  console.log('Received:', data);
});

ws.on('error', function(error) {
  console.error('WebSocket error:', error);
});

ws.on('close', function() {
  console.log('WebSocket closed.');
});
