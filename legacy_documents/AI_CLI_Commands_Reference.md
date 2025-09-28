# Comprehensive AI CLI Commands Reference

This document provides a comprehensive reference for CLI commands for various AI development tools: OpenAI (Codex), Google Gemini, Claude Code, and Qwen.

## 1. OpenAI Codex CLI Commands

**Note: OpenAI Codex has been discontinued as of July 2023.** The functionality has been superseded by the OpenAI API and models like GPT-4 and GPT-3.5 Turbo. The Codex-specific tools and CLI have been deprecated.

### Historical Context
- Codex was primarily accessed through the OpenAI API rather than a dedicated CLI tool
- Development was focused on integration with IDEs and programming environments
- The main product now is the OpenAI API for code generation and assistance

## 2. Google Gemini CLI Commands

The Google Gemini CLI provides a command-line interface for interacting with Google's Gemini AI models.

### Installation
```bash
npm install -g @google/gemini-cli
```

### Basic Commands
```bash
# Start interactive chat session
gemini

# Send a single query and get response
gemini "What is the weather today?"

# View help information
gemini --help
```

### Advanced Options
```bash
# Specify model version
gemini --model gemini-pro "Explain quantum computing"

# Set temperature for response creativity
gemini --temperature 0.7 "Write a creative story"

# Set maximum output tokens
gemini --max-tokens 1024 "Summarize this article"
```

### File Processing
```bash
# Process and analyze a file
gemini file.txt "Explain this code"

# Process PDF files
gemini document.pdf "Extract key points"
```

### Configuration
```bash
# Configure API key
gemini config --key YOUR_API_KEY

# View current configuration
gemini config --view

# Reset configuration
gemini config --reset
```

## 3. Claude Code CLI Commands

Claude Code provides a comprehensive CLI for AI-assisted development workflows.

### Basic Commands
```bash
# Start interactive REPL
claude

# Start REPL with initial prompt
claude "explain this project"

# Query via SDK, then exit
claude -p "explain this function"

# Process piped content
cat logs.txt | claude -p "explain"
```

### Session Management
```bash
# Continue most recent conversation
claude -c

# Continue via SDK
claude -c -p "Check for type errors"

# Resume session by ID
claude -r "abc123" "Finish this PR"

# Update to latest version
claude update
```

### Model Configuration
```bash
# Specify model for session
claude --model claude-sonnet-4-20250514

# Set maximum number of turns in non-interactive mode
claude -p --max-turns 3 "query"
```

### File and Directory Access
```bash
# Add additional working directories
claude --add-dir ../apps ../lib

# Process content in specific directory context
claude --add-dir ./src "analyze these files"
```

### Output Formatting
```bash
# Print response without interactive mode
claude -p "query"

# Specify output format (text, json, stream-json)
claude -p "query" --output-format json

# Specify input format (text, stream-json)
claude -p --output-format json --input-format stream-json

# Include partial streaming events
claude -p --output-format stream-json --include-partial-messages "query"
```

### Permissions and Safety
```bash
# List of tools allowed without prompting
claude --allowedTools "Bash(git log:*)" "Read"

# List of tools disallowed without prompting
claude --disallowedTools "Edit" "Bash(rm:*)"

# Begin in specified permission mode
claude --permission-mode plan

# Skip permission prompts (use with caution)
claude --dangerously-skip-permissions

# Specify MCP tool for permission prompts in non-interactive mode
claude -p --permission-prompt-tool mcp_auth_tool "query"
```

### Debugging and Verbose Output
```bash
# Enable verbose logging
claude --verbose

# Verbose logging in print mode
claude -p --verbose "query"
```

### MCP (Model Context Protocol) Configuration
```bash
# Configure MCP servers
claude mcp
```

## 4. Claude Code Templates CLI

Additional CLI tool for configuring and monitoring Claude Code components.

### Installation and Setup
```bash
# Interactive browser installation
npx claude-code-templates@latest

# Complete development stack installation
npx claude-code-templates@latest --agent frontend-developer --command generate-tests --mcp github-integration
```

### Component Installation
```bash
# Install specific agent
npx claude-code-templates@latest --agent security-auditor

# Install specific command
npx claude-code-templates@latest --command optimize-bundle

# Install specific setting
npx claude-code-templates@latest --setting mcp-timeouts

# Install hook
npx claude-code-templates@latest --hook pre-commit-validation

# Install MCP integration
npx claude-code-templates@latest --mcp postgresql-integration
```

### Monitoring and Analytics
```bash
# Monitor analytics
npx claude-code-templates@latest --analytics

# View Claude conversations (local access)
npx claude-code-templates@latest --chats

# View Claude conversations (secure remote access)
npx claude-code-templates@latest --chats --tunnel

# Check installation health
npx claude-code-templates@latest --health-check
```

## 5. Qwen Code CLI Commands

Qwen Code is a command-line AI workflow tool that provides AI-powered assistance for coding tasks.

### Installation
```bash
pip install qwen-code
```

### Basic Usage
```bash
# Start interactive session
qwen-code

# Run a single command
qwen-code --prompt "Explain this Python code"

# Process a file
qwen-code --file mycode.py --prompt "Review this code"
```

### Code Assistance Commands
```bash
# Generate code
qwen-code --generate --prompt "Create a function to sort an array"

# Explain code
qwen-code --explain --file mycode.py

# Debug code
qwen-code --debug --file mycode.py --error "TypeError: unsupported operand"

# Optimize code
qwen-code --optimize --file mycode.py
```

### Project Context
```bash
# Analyze entire project
qwen-code --project /path/to/project --prompt "Summarize this project"

# Search in project context
qwen-code --search --query "find all database connections"
```

### Configuration
```bash
# Configure API key
qwen-code config --set api_key "your-api-key"

# View current configuration
qwen-code config --view

# Reset configuration
qwen-code config --reset
```

### Advanced Features
```bash
# Run in streaming mode
qwen-code --stream --prompt "Write a Python script for..."

# Set model parameters
qwen-code --temperature 0.7 --top-p 0.9 --prompt "Write code..."

# Use specific model
qwen-code --model qwen2.5-coder --prompt "Help with this issue"
```

### Integration Commands
```bash
# Git integration
qwen-code --git --prompt "Explain recent changes"

# Issue tracking integration
qwen-code --issue --prompt "Create fix for issue #123"

# Testing assistance
qwen-code --test --file mycode.py --prompt "Generate unit tests"
```

## Additional Resources

- OpenAI API Documentation: https://platform.openai.com/docs/
- Google Gemini API Documentation: https://ai.google.dev/
- Anthropic Claude Documentation: https://docs.anthropic.com/
- Qwen Documentation: https://qwen.ai/

Each of these tools provides powerful AI assistance for coding and development tasks. Choose the one that best fits your workflow and requirements.

# Comprehensive AI CLI Commands Reference

This document provides a comprehensive reference for CLI commands for various AI development tools: OpenAI (Codex), Google Gemini, Claude Code, and Qwen.

## 1. OpenAI Codex CLI Commands

**Note: OpenAI Codex has been discontinued as of July 2023.** The functionality has been superseded by the OpenAI API and models like GPT-4 and GPT-3.5 Turbo. The Codex-specific tools and CLI have been deprecated.

### Historical Context
- Codex was primarily accessed through the OpenAI API rather than a dedicated CLI tool
- Development was focused on integration with IDEs and programming environments
- The main product now is the OpenAI API for code generation and assistance

## 2. Google Gemini CLI Commands

The Google Gemini CLI provides a command-line interface for interacting with Google's Gemini AI models.

### Installation
```bash
npm install -g @google/gemini-cli
```

### Basic Commands
```bash
# Start interactive chat session
gemini

# Send a single query and get response
gemini "What is the weather today?"

# View help information
gemini --help
```

### Advanced Options
```bash
# Specify model version
gemini --model gemini-pro "Explain quantum computing"

# Set temperature for response creativity
gemini --temperature 0.7 "Write a creative story"

# Set maximum output tokens
gemini --max-tokens 1024 "Summarize this article"
```

### File Processing
```bash
# Process and analyze a file
gemini file.txt "Explain this code"

# Process PDF files
gemini document.pdf "Extract key points"
```

### Configuration
```bash
# Configure API key
gemini config --key YOUR_API_KEY

# View current configuration
gemini config --view

# Reset configuration
gemini config --reset
```

## 3. Claude Code CLI Commands

Claude Code provides a comprehensive CLI for AI-assisted development workflows.

### Basic Commands
```bash
# Start interactive REPL
claude

# Start REPL with initial prompt
claude "explain this project"

# Query via SDK, then exit
claude -p "explain this function"

# Process piped content
cat logs.txt | claude -p "explain"
```

### Session Management
```bash
# Continue most recent conversation
claude -c

# Continue via SDK
claude -c -p "Check for type errors"

# Resume session by ID
claude -r "abc123" "Finish this PR"

# Update to latest version
claude update
```

### Model Configuration
```bash
# Specify model for session
claude --model claude-sonnet-4-20250514

# Set maximum number of turns in non-interactive mode
claude -p --max-turns 3 "query"
```

### File and Directory Access
```bash
# Add additional working directories
claude --add-dir ../apps ../lib

# Process content in specific directory context
claude --add-dir ./src "analyze these files"
```

### Output Formatting
```bash
# Print response without interactive mode
claude -p "query"

# Specify output format (text, json, stream-json)
claude -p "query" --output-format json

# Specify input format (text, stream-json)
claude -p --output-format json --input-format stream-json

# Include partial streaming events
claude -p --output-format stream-json --include-partial-messages "query"
```

### Permissions and Safety
```bash
# List of tools allowed without prompting
claude --allowedTools "Bash(git log:*)" "Read"

# List of tools disallowed without prompting
claude --disallowedTools "Edit" "Bash(rm:*)"

# Begin in specified permission mode
claude --permission-mode plan

# Skip permission prompts (use with caution)
claude --dangerously-skip-permissions

# Specify MCP tool for permission prompts in non-interactive mode
claude -p --permission-prompt-tool mcp_auth_tool "query"
```

### Debugging and Verbose Output
```bash
# Enable verbose logging
claude --verbose

# Verbose logging in print mode
claude -p --verbose "query"
```

### MCP (Model Context Protocol) Configuration
```bash
# Configure MCP servers
claude mcp
```

## 4. Claude Code Templates CLI

Additional CLI tool for configuring and monitoring Claude Code components.

### Installation and Setup
```bash
# Interactive browser installation
npx claude-code-templates@latest

# Complete development stack installation
npx claude-code-templates@latest --agent frontend-developer --command generate-tests --mcp github-integration
```

### Component Installation
```bash
# Install specific agent
npx claude-code-templates@latest --agent security-auditor

# Install specific command
npx claude-code-templates@latest --command optimize-bundle

# Install specific setting
npx claude-code-templates@latest --setting mcp-timeouts

# Install hook
npx claude-code-templates@latest --hook pre-commit-validation

# Install MCP integration
npx claude-code-templates@latest --mcp postgresql-integration
```

### Monitoring and Analytics
```bash
# Monitor analytics
npx claude-code-templates@latest --analytics

# View Claude conversations (local access)
npx claude-code-templates@latest --chats

# View Claude conversations (secure remote access)
npx claude-code-templates@latest --chats --tunnel

# Check installation health
npx claude-code-templates@latest --health-check
```

## 5. Qwen Code CLI Commands

Qwen Code is a command-line AI workflow tool that provides AI-powered assistance for coding tasks.

### Installation
```bash
pip install qwen-code
```

### Basic Usage
```bash
# Start interactive session
qwen-code

# Run a single command
qwen-code --prompt "Explain this Python code"

# Process a file
qwen-code --file mycode.py --prompt "Review this code"
```

### Code Assistance Commands
```bash
# Generate code
qwen-code --generate --prompt "Create a function to sort an array"

# Explain code
qwen-code --explain --file mycode.py

# Debug code
qwen-code --debug --file mycode.py --error "TypeError: unsupported operand"

# Optimize code
qwen-code --optimize --file mycode.py
```

### Project Context
```bash
# Analyze entire project
qwen-code --project /path/to/project --prompt "Summarize this project"

# Search in project context
qwen-code --search --query "find all database connections"
```

### Configuration
```bash
# Configure API key
qwen-code config --set api_key "your-api-key"

# View current configuration
qwen-code config --view

# Reset configuration
qwen-code config --reset
```

### Advanced Features
```bash
# Run in streaming mode
qwen-code --stream --prompt "Write a Python script for..."

# Set model parameters
qwen-code --temperature 0.7 --top-p 0.9 --prompt "Write code..."

# Use specific model
qwen-code --model qwen2.5-coder --prompt "Help with this issue"
```

### Integration Commands
```bash
# Git integration
qwen-code --git --prompt "Explain recent changes"

# Issue tracking integration
qwen-code --issue --prompt "Create fix for issue #123"

# Testing assistance
qwen-code --test --file mycode.py --prompt "Generate unit tests"
```

## Additional Resources

- OpenAI API Documentation: https://platform.openai.com/docs/
- Google Gemini API Documentation: https://ai.google.dev/
- Anthropic Claude Documentation: https://docs.anthropic.com/
- Qwen Documentation: https://qwen.ai/

Each of these tools provides powerful AI assistance for coding and development tasks. Choose the one that best fits your workflow and requirements.