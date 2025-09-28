# AI Interaction Command

Send messages to any Rod-Corp AI agent and get results through the AI Interaction Server.

## Usage
Interact with AI agents directly from Claude Code, with automatic file handling and result processing.

## Implementation
```bash
#!/bin/bash
# Enhanced AI Interaction with Error Handling

# Standardized output functions
print_header() {
    echo "🚀 $1"
    echo "========================"
}

print_success() {
    echo "✅ $1"
}

print_warning() {
    echo "⚠️  $1"
}

print_error() {
    echo "❌ $1"
}

print_info() {
    echo "ℹ️  $1"
}

# Error handling
set -e

# Default values
AGENT="claude-full"
MESSAGE=""
CONTEXT=""
RETURN_FILES="true"
TIMEOUT=300

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --agent)
            AGENT="$2"
            shift 2
            ;;
        --message)
            MESSAGE="$2"
            shift 2
            ;;
        --context)
            CONTEXT="$2"
            shift 2
            ;;
        --no-files)
            RETURN_FILES="false"
            shift
            ;;
        --timeout)
            TIMEOUT="$2"
            shift 2
            ;;
        --help)
            echo "AI Interaction Command"
            echo "====================="
            echo "Send messages to Rod-Corp AI agents"
            echo
            echo "Usage:"
            echo "  /ai-interact --agent <agent> --message \"<message>\" [--context \"<context>\"]"
            echo
            echo "Options:"
            echo "  --agent <agent>      AI agent to use (claude-full, qwen-full, etc.)"
            echo "  --message \"<text>\"   Message to send to the agent"
            echo "  --context \"<text>\"   Optional context for the agent"
            echo "  --no-files          Don't return generated files"
            echo "  --timeout <seconds> Timeout for the request (default: 300)"
            echo "  --help              Show this help"
            exit 0
            ;;
        *)
            print_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Validate required parameters
if [ -z "$MESSAGE" ]; then
    print_error "Message is required. Use --message \"<your message>\""
    exit 1
fi

print_header "AI Interaction with $AGENT"

# Check if AI Interaction Server is running
print_info "Checking AI Interaction Server status..."
if ! curl -s -f "http://localhost:49152/health" >/dev/null 2>&1; then
    print_warning "AI Interaction Server not responding. Attempting to start..."
    cd /home/rod/rod-corp/services/ai-interaction-server
    if [ -f "./start.sh" ]; then
        ./start.sh >/dev/null 2>&1 &
        sleep 5
        if ! curl -s -f "http://localhost:49152/health" >/dev/null 2>&1; then
            print_error "Failed to start AI Interaction Server"
            exit 1
        else
            print_success "AI Interaction Server started successfully"
        fi
    else
        print_error "AI Interaction Server start script not found"
        exit 1
    fi
else
    print_success "AI Interaction Server is running"
fi

# Send message to AI agent
print_info "Sending message to $AGENT..."
REQUEST_DATA=$(jq -n \
    --arg agent "$AGENT" \
    --arg message "$MESSAGE" \
    --arg context "$CONTEXT" \
    --argjson return_files "$RETURN_FILES" \
    '{
        agent: $agent,
        message: $message,
        context: $context,
        return_files: $return_files
    }')

RESPONSE=$(curl -s -X POST "http://localhost:49152/interact" \
    -H "Content-Type: application/json" \
    -d "$REQUEST_DATA" \
    --max-time "$TIMEOUT")

# Check for errors
if echo "$RESPONSE" | jq -e '.error' >/dev/null 2>&1; then
    ERROR_MSG=$(echo "$RESPONSE" | jq -r '.error')
    print_error "AI Interaction failed: $ERROR_MSG"
    exit 1
fi

# Get request ID
REQUEST_ID=$(echo "$RESPONSE" | jq -r '.request_id')
if [ "$REQUEST_ID" = "null" ] || [ -z "$REQUEST_ID" ]; then
    print_error "Failed to get request ID from response"
    echo "Response: $RESPONSE"
    exit 1
fi

print_success "Request submitted successfully (ID: $REQUEST_ID)"

# Wait for completion
print_info "Waiting for AI agent to process request..."
SECONDS_WAITED=0
MAX_WAIT=300  # 5 minutes

while [ $SECONDS_WAITED -lt $MAX_WAIT ]; do
    RESULT=$(curl -s "http://localhost:49152/results/$REQUEST_ID")
    
    STATUS=$(echo "$RESULT" | jq -r '.status')
    if [ "$STATUS" = "null" ] || [ -z "$STATUS" ]; then
        print_error "Failed to get status from response"
        echo "Response: $RESULT"
        exit 1
    fi
    
    case "$STATUS" in
        "completed")
            print_success "AI agent completed processing"
            break
            ;;
        "failed")
            ERROR=$(echo "$RESULT" | jq -r '.error')
            print_error "AI agent failed: $ERROR"
            exit 1
            ;;
        "processing")
            # Still processing, wait and continue
            sleep 2
            SECONDS_WAITED=$((SECONDS_WAITED + 2))
            ;;
        *)
            print_error "Unknown status: $STATUS"
            echo "Response: $RESULT"
            exit 1
            ;;
    esac
done

if [ $SECONDS_WAITED -ge $MAX_WAIT ]; then
    print_error "Timeout waiting for AI agent to complete processing"
    exit 1
fi

# Display results
echo
print_header "AI Agent Response"
echo "$RESULT" | jq -r '.response'

# Handle files if any
FILES=$(echo "$RESULT" | jq -r '.files // empty')
if [ -n "$FILES" ] && [ "$FILES" != "[]" ]; then
    echo
    print_header "Generated Files"
    echo "$FILES" | jq -r '.[]' | while read -r FILE; do
        print_info "File: $FILE"
        
        # Download file
        if [ "$RETURN_FILES" = "true" ]; then
            FILENAME=$(basename "$FILE")
            curl -s "http://localhost:49152/download/$REQUEST_ID/$FILENAME" -o "$FILENAME"
            if [ $? -eq 0 ]; then
                print_success "Downloaded: $FILENAME ($(stat -c%s "$FILENAME" 2>/dev/null || echo "unknown") bytes)"
            else
                print_error "Failed to download: $FILENAME"
            fi
        fi
    done
fi

print_success "AI Interaction completed successfully!"
echo "💡 Tip: Use '/ai-interact --help' for more options"
```

## Options
- `--agent <agent>`: Specify which AI agent to use (default: claude-full)
- `--message "<text>"`: Message to send to the agent
- `--context "<text>"`: Additional context for the agent
- `--no-files`: Don't return generated files
- `--timeout <seconds>`: Timeout for the request (default: 300)
- `--help`: Show help information

## Examples
```bash
# Simple interaction
/ai-interact --agent "claude-full" --message "Write a Python function to calculate Fibonacci numbers"

# With context
/ai-interact --agent "qwen-full" --message "Optimize this code" --context "Performance-critical data processing pipeline"

# No file return
/ai-interact --agent "deepseek-full" --message "Explain quantum computing" --no-files

# With timeout
/ai-interact --agent "mixtral-full" --message "Analyze this dataset" --timeout 600
```

## Features
- **Error Handling**: Comprehensive error checking and fallback mechanisms
- **Automatic Server Management**: Starts AI Interaction Server if not running
- **File Handling**: Automatically downloads generated files
- **Progress Monitoring**: Real-time status updates
- **Timeout Protection**: Prevents hanging requests
- **Standardized Output**: Consistent formatting with visual indicators