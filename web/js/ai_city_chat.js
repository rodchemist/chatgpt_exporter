/**
 * AI City Chat Interface JavaScript
 * Handles API communication, WebSocket connections, UI interactions, and theme management
 */

class AICityChat {
  constructor() {
    this.apiBaseUrl = 'http://localhost:9000';
    this.websocketUrl = 'ws://localhost:8765';
    this.websocketUrl2 = 'ws://localhost:8766';
    this.websocket = null;
    this.reconnectAttempts = 0;
    this.maxReconnectAttempts = 5;
    this.reconnectDelay = 2000;
    this.messageHistory = [];
    this.isTyping = false;

    // DOM elements
    this.elements = {};

    // Initialize when DOM is loaded
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => this.init());
    } else {
      this.init();
    }
  }

  init() {
    this.initializeElements();
    this.setupEventListeners();
    this.loadTheme();
    this.initializeConnection();
    this.loadServices();
    this.setupAutoResize();
  }

  initializeElements() {
    this.elements = {
      connectionStatus: document.getElementById('connectionStatus'),
      statusIndicator: document.getElementById('statusIndicator'),
      statusText: document.getElementById('statusText'),
      themeToggle: document.getElementById('themeToggle'),
      infoButton: document.getElementById('infoButton'),
      sidebar: document.getElementById('sidebar'),
      closeSidebar: document.getElementById('closeSidebar'),
      servicesList: document.getElementById('servicesList'),
      chatMessages: document.getElementById('chatMessages'),
      typingIndicator: document.getElementById('typingIndicator'),
      messageInput: document.getElementById('messageInput'),
      sendButton: document.getElementById('sendButton'),
      characterCount: document.getElementById('characterCount'),
      clearChat: document.getElementById('clearChat'),
      exportChat: document.getElementById('exportChat'),
      connectionModal: document.getElementById('connectionModal'),
      connectionMessage: document.getElementById('connectionMessage'),
      retryConnection: document.getElementById('retryConnection')
    };
  }

  setupEventListeners() {
    // Theme toggle
    this.elements.themeToggle.addEventListener('click', () => this.toggleTheme());

    // Sidebar toggle
    this.elements.infoButton.addEventListener('click', () => this.toggleSidebar());
    this.elements.closeSidebar.addEventListener('click', () => this.closeSidebar());

    // Message input
    this.elements.messageInput.addEventListener('input', (e) => {
      this.updateCharacterCount();
      this.updateSendButton();
      this.autoResizeTextarea();
    });

    this.elements.messageInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        this.sendMessage();
      }
    });

    // Send button
    this.elements.sendButton.addEventListener('click', () => this.sendMessage());

    // Quick actions
    this.elements.clearChat.addEventListener('click', () => this.clearChat());
    this.elements.exportChat.addEventListener('click', () => this.exportChat());

    // Connection modal
    this.elements.retryConnection.addEventListener('click', () => this.retryConnection());

    // Click outside sidebar to close
    document.addEventListener('click', (e) => {
      if (this.elements.sidebar.classList.contains('open') &&
          !this.elements.sidebar.contains(e.target) &&
          !this.elements.infoButton.contains(e.target)) {
        this.closeSidebar();
      }
    });

    // Handle window resize
    window.addEventListener('resize', () => this.handleResize());
  }

  async initializeConnection() {
    this.updateConnectionStatus('connecting', 'Connecting to AI City...');

    try {
      // Test REST API connection
      const response = await fetch(`${this.apiBaseUrl}/api/health`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        this.updateConnectionStatus('connected', 'Connected to AI City');
        this.hideConnectionModal();
        this.initializeWebSocket();
      } else {
        throw new Error('API not responding');
      }
    } catch (error) {
      console.error('Connection error:', error);
      this.updateConnectionStatus('disconnected', 'Failed to connect');
      this.showConnectionModal('Failed to connect to AI City API. Please ensure the server is running on localhost:9000.');
    }
  }

  initializeWebSocket() {
    try {
      this.websocket = new WebSocket(this.websocketUrl);

      this.websocket.onopen = () => {
        console.log('WebSocket connected');
        this.reconnectAttempts = 0;
      };

      this.websocket.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          this.handleWebSocketMessage(data);
        } catch (error) {
          console.error('Error parsing WebSocket message:', error);
        }
      };

      this.websocket.onclose = () => {
        console.log('WebSocket disconnected');
        this.attemptWebSocketReconnect();
      };

      this.websocket.onerror = (error) => {
        console.error('WebSocket error:', error);
      };
    } catch (error) {
      console.error('Failed to initialize WebSocket:', error);
    }
  }

  attemptWebSocketReconnect() {
    if (this.reconnectAttempts < this.maxReconnectAttempts) {
      this.reconnectAttempts++;
      console.log(`Attempting WebSocket reconnection ${this.reconnectAttempts}/${this.maxReconnectAttempts}`);

      setTimeout(() => {
        this.initializeWebSocket();
      }, this.reconnectDelay * this.reconnectAttempts);
    }
  }

  handleWebSocketMessage(data) {
    if (data.type === 'typing') {
      this.showTypingIndicator();
    } else if (data.type === 'message') {
      this.hideTypingIndicator();
      this.addMessage('ai', data.content, data.agent || 'AI City');
    } else if (data.type === 'status') {
      this.updateConnectionStatus(data.status, data.message);
    }
  }

  async sendMessage() {
    const message = this.elements.messageInput.value.trim();
    if (!message) return;

    // Add user message to chat
    this.addMessage('user', message);
    this.elements.messageInput.value = '';
    this.updateCharacterCount();
    this.updateSendButton();
    this.autoResizeTextarea();

    // Show typing indicator
    this.showTypingIndicator();

    try {
      const response = await fetch(`${this.apiBaseUrl}/api/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: message,
          user_id: "rod",
          chat_type: "direct"
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      const data = await response.json();

      // Hide typing indicator
      this.hideTypingIndicator();

      // Add AI response to chat
      if (data.response) {
        this.addMessage('ai', data.response, data.agent || 'AI City');
      } else if (data.error) {
        this.addMessage('ai', `Error: ${data.error}`, 'System');
      } else {
        this.addMessage('ai', 'Received response from AI City.', 'AI City');
      }

    } catch (error) {
      console.error('Error sending message:', error);
      this.hideTypingIndicator();
      this.addMessage('ai', `Connection error: ${error.message}. Please check if the AI City server is running.`, 'System');
    }
  }

  addMessage(type, content, sender = null) {
    const messageData = {
      type,
      content,
      sender,
      timestamp: new Date()
    };

    this.messageHistory.push(messageData);

    const messageElement = document.createElement('div');
    messageElement.className = `message ${type}`;

    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';
    messageContent.textContent = content;

    const messageMeta = document.createElement('div');
    messageMeta.className = 'message-meta';

    const timeString = messageData.timestamp.toLocaleTimeString([], {
      hour: '2-digit',
      minute: '2-digit'
    });

    if (type === 'ai' && sender) {
      messageMeta.textContent = `${sender} • ${timeString}`;
    } else {
      messageMeta.textContent = timeString;
    }

    messageElement.appendChild(messageContent);
    messageElement.appendChild(messageMeta);

    // Remove welcome message if it exists
    const welcomeMessage = this.elements.chatMessages.querySelector('.welcome-message');
    if (welcomeMessage) {
      welcomeMessage.remove();
    }

    this.elements.chatMessages.appendChild(messageElement);
    this.scrollToBottom();
  }

  showTypingIndicator() {
    if (!this.isTyping) {
      this.isTyping = true;
      this.elements.typingIndicator.classList.add('show');
      this.scrollToBottom();
    }
  }

  hideTypingIndicator() {
    if (this.isTyping) {
      this.isTyping = false;
      this.elements.typingIndicator.classList.remove('show');
    }
  }

  scrollToBottom() {
    requestAnimationFrame(() => {
      this.elements.chatMessages.scrollTop = this.elements.chatMessages.scrollHeight;
    });
  }

  updateCharacterCount() {
    const length = this.elements.messageInput.value.length;
    const maxLength = this.elements.messageInput.maxLength;
    this.elements.characterCount.textContent = `${length}/${maxLength}`;

    if (length > maxLength * 0.9) {
      this.elements.characterCount.style.color = 'var(--error-color)';
    } else if (length > maxLength * 0.7) {
      this.elements.characterCount.style.color = 'var(--warning-color)';
    } else {
      this.elements.characterCount.style.color = 'var(--text-muted)';
    }
  }

  updateSendButton() {
    const hasText = this.elements.messageInput.value.trim().length > 0;
    this.elements.sendButton.disabled = !hasText;
  }

  autoResizeTextarea() {
    const textarea = this.elements.messageInput;
    textarea.style.height = 'auto';
    const newHeight = Math.min(textarea.scrollHeight, 120);
    textarea.style.height = newHeight + 'px';
  }

  setupAutoResize() {
    // Initial setup
    this.autoResizeTextarea();
    this.updateSendButton();
    this.updateCharacterCount();
  }

  toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('ai-city-theme', newTheme);

    // Update theme icon
    const icon = this.elements.themeToggle.querySelector('.theme-icon');
    icon.textContent = newTheme === 'dark' ? '☀️' : '🌙';
  }

  loadTheme() {
    const savedTheme = localStorage.getItem('ai-city-theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);

    const icon = this.elements.themeToggle.querySelector('.theme-icon');
    icon.textContent = savedTheme === 'dark' ? '☀️' : '🌙';
  }

  toggleSidebar() {
    this.elements.sidebar.classList.add('open');
  }

  closeSidebar() {
    this.elements.sidebar.classList.remove('open');
  }

  async loadServices() {
    try {
      const response = await fetch(`${this.apiBaseUrl}/api/services`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        const services = await response.json();
        this.displayServices(services);
      } else {
        throw new Error('Failed to load services');
      }
    } catch (error) {
      console.error('Error loading services:', error);
      this.displayDefaultServices();
    }
  }

  displayServices(services) {
    const servicesList = this.elements.servicesList;
    servicesList.innerHTML = '';

    if (services && services.length > 0) {
      services.forEach(service => {
        const serviceElement = document.createElement('div');
        serviceElement.className = 'service-item';

        serviceElement.innerHTML = `
          <div class="service-name">${service.name || 'Unknown Service'}</div>
          <div class="service-description">${service.description || 'No description available'}</div>
        `;

        servicesList.appendChild(serviceElement);
      });
    } else {
      this.displayDefaultServices();
    }
  }

  displayDefaultServices() {
    const servicesList = this.elements.servicesList;
    servicesList.innerHTML = `
      <div class="service-item">
        <div class="service-name">🤖 AI Orchestration</div>
        <div class="service-description">Central coordination of AI agents</div>
      </div>
      <div class="service-item">
        <div class="service-name">🔍 Research Agent</div>
        <div class="service-description">Information gathering and analysis</div>
      </div>
      <div class="service-item">
        <div class="service-name">📚 Knowledge Base</div>
        <div class="service-description">Document storage and retrieval</div>
      </div>
      <div class="service-item">
        <div class="service-name">🛠️ Tool Integration</div>
        <div class="service-description">External tool management</div>
      </div>
      <div class="service-item">
        <div class="service-name">📊 Analytics</div>
        <div class="service-description">Data analysis and reporting</div>
      </div>
      <div class="service-item">
        <div class="service-name">🔗 API Gateway</div>
        <div class="service-description">Request routing and management</div>
      </div>
      <div class="service-item">
        <div class="service-name">💬 Communication Hub</div>
        <div class="service-description">Multi-agent communication</div>
      </div>
      <div class="service-item">
        <div class="service-name">🔐 Security Manager</div>
        <div class="service-description">Authentication and authorization</div>
      </div>
    `;
  }

  updateConnectionStatus(status, message) {
    this.elements.statusIndicator.className = `status-indicator ${status}`;
    this.elements.statusText.textContent = message;
  }

  showConnectionModal(message) {
    this.elements.connectionMessage.textContent = message;
    this.elements.connectionModal.classList.add('show');
  }

  hideConnectionModal() {
    this.elements.connectionModal.classList.remove('show');
  }

  retryConnection() {
    this.hideConnectionModal();
    this.initializeConnection();
  }

  clearChat() {
    if (confirm('Are you sure you want to clear the chat history?')) {
      this.messageHistory = [];
      this.elements.chatMessages.innerHTML = `
        <div class="welcome-message">
          <div class="welcome-icon">🏙️</div>
          <h2>Welcome to AI City</h2>
          <p>Connect with our specialized AI agents and services. Start a conversation below!</p>
        </div>
      `;
    }
  }

  exportChat() {
    if (this.messageHistory.length === 0) {
      alert('No messages to export.');
      return;
    }

    const exportData = {
      timestamp: new Date().toISOString(),
      messages: this.messageHistory,
      totalMessages: this.messageHistory.length
    };

    const dataStr = JSON.stringify(exportData, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });

    const link = document.createElement('a');
    link.href = URL.createObjectURL(dataBlob);
    link.download = `ai-city-chat-${new Date().toISOString().split('T')[0]}.json`;

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  handleResize() {
    // Close sidebar on mobile when resizing to larger screen
    if (window.innerWidth > 768 && this.elements.sidebar.classList.contains('open')) {
      this.closeSidebar();
    }
  }
}

// Initialize the chat application
const aiCityChat = new AICityChat();