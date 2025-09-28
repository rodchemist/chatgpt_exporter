# AI City Chat Interface

A modern, responsive web-based chat interface for the AI City running on localhost:9000.

## Features

### 🎨 Modern Design
- Clean, professional interface with smooth animations
- Dark/light theme toggle
- Mobile-friendly responsive design
- Real-time typing indicators

### 🔌 Connectivity
- REST API integration with localhost:9000/api/chat
- WebSocket support for real-time messaging (ports 8765/8766)
- Automatic connection status monitoring
- Connection retry mechanism with exponential backoff

### 💬 Chat Features
- Real-time messaging with AI City agents
- Message history with timestamps
- Character count with visual feedback
- Auto-resizing text input
- Export chat history to JSON

### 🛠️ Technical Features
- Pure HTML/CSS/JavaScript (no frameworks)
- CORS-ready for local development
- Error handling for connection issues
- Responsive design for all screen sizes
- Accessibility features

## File Structure

```
web/
├── launch_ai_city_chat.html     # Launcher page
├── html/
│   └── ai_city_chat.html        # Main chat interface
├── css/
│   └── ai_city_chat.css         # Comprehensive styles
├── js/
│   └── ai_city_chat.js          # Chat functionality
└── AI_CITY_CHAT_README.md       # This file
```

## Quick Start

### Option 1: Use the Launcher
1. Open `launch_ai_city_chat.html` in your web browser
2. Click "Launch Chat Interface" or wait for auto-redirect

### Option 2: Direct Access
1. Open `html/ai_city_chat.html` directly in your web browser

## Prerequisites

### AI City Server
Ensure your AI City server is running on:
- **REST API**: `http://localhost:9000`
- **WebSocket**: `ws://localhost:8765` or `ws://localhost:8766`

### Browser Requirements
- Modern web browser (Chrome 70+, Firefox 65+, Safari 12+, Edge 79+)
- JavaScript enabled
- Local file access (for file:// protocol) or serve via HTTP server

## Usage Instructions

### Starting a Conversation
1. Type your message in the text input at the bottom
2. Press Enter or click the send button (📤)
3. Wait for the AI City response

### Interface Controls
- **Theme Toggle** (🌙/☀️): Switch between dark and light themes
- **Info Button** (ℹ️): Show available services and API information
- **Clear Chat** (🗑️): Clear all messages (with confirmation)
- **Export Chat** (💾): Download chat history as JSON file

### Keyboard Shortcuts
- **Enter**: Send message
- **Shift + Enter**: New line in message
- **Escape**: Close sidebar (if open)

## API Integration

### REST API Endpoint
```
POST http://localhost:9000/api/chat
Content-Type: application/json

{
  "message": "Your message here",
  "timestamp": "2024-01-01T12:00:00.000Z"
}
```

### Expected Response
```json
{
  "response": "AI response text",
  "agent": "Agent Name",
  "timestamp": "2024-01-01T12:00:00.000Z"
}
```

### WebSocket Messages
The interface supports real-time WebSocket messages:

```json
{
  "type": "typing",
  "agent": "Agent Name"
}

{
  "type": "message",
  "content": "Response text",
  "agent": "Agent Name"
}

{
  "type": "status",
  "status": "connected|disconnected|error",
  "message": "Status message"
}
```

## Customization

### Theme Customization
Edit CSS variables in `ai_city_chat.css`:

```css
:root {
  --primary-color: #2563eb;      /* Primary blue */
  --background-color: #ffffff;   /* Light background */
  --text-primary: #0f172a;       /* Dark text */
  /* ... more variables */
}

[data-theme="dark"] {
  --primary-color: #3b82f6;      /* Darker blue */
  --background-color: #0f172a;   /* Dark background */
  --text-primary: #f8fafc;       /* Light text */
  /* ... dark theme overrides */
}
```

### API Configuration
Modify API endpoints in `ai_city_chat.js`:

```javascript
this.apiBaseUrl = 'http://localhost:9000';
this.websocketUrl = 'ws://localhost:8765';
this.websocketUrl2 = 'ws://localhost:8766';
```

## Troubleshooting

### Connection Issues
1. **"Failed to connect to AI City API"**
   - Verify AI City server is running on localhost:9000
   - Check for CORS issues
   - Ensure API endpoint `/api/chat` is available

2. **WebSocket Connection Failed**
   - Check if WebSocket server is running on port 8765 or 8766
   - Verify firewall settings
   - Try refreshing the page

3. **Interface Not Loading**
   - Check browser console for JavaScript errors
   - Ensure all files are in correct locations
   - Try serving files via HTTP server instead of file:// protocol

### Performance Issues
1. **Slow Response Times**
   - Check AI City server performance
   - Monitor network requests in browser dev tools
   - Consider message length limits

2. **Memory Usage**
   - Chat history is stored in memory
   - Use "Clear Chat" for long conversations
   - Export and clear periodically for best performance

## Browser Compatibility

| Browser | Version | Status |
|---------|---------|--------|
| Chrome  | 70+     | ✅ Full Support |
| Firefox | 65+     | ✅ Full Support |
| Safari  | 12+     | ✅ Full Support |
| Edge    | 79+     | ✅ Full Support |
| IE      | Any     | ❌ Not Supported |

## Security Considerations

- Interface designed for local development use
- No authentication implemented (relies on AI City server)
- WebSocket connections are unencrypted (ws://)
- For production use, implement HTTPS/WSS and authentication

## Contributing

To enhance the chat interface:

1. **HTML**: Modify `html/ai_city_chat.html` for structure changes
2. **CSS**: Update `css/ai_city_chat.css` for styling
3. **JavaScript**: Edit `js/ai_city_chat.js` for functionality
4. **Testing**: Test with actual AI City server running

## License

This chat interface is part of the AI City Documentation Center project.

---

**Need Help?** Check the browser console for detailed error messages and ensure your AI City server is properly configured and running.