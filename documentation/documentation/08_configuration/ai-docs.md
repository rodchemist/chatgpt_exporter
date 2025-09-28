# AI System Documentation Navigator

Quick access to AI system documentation and help resources.

## Usage
Navigate and search through the comprehensive AI system documentation, including troubleshooting guides, integration details, and system architecture.

## Implementation
```bash
echo "📚 AI System Documentation Navigator"
echo "===================================="

DOC_DIR="/home/rod/rod-corp/docs/ai-agents"

# Check if documentation exists
if [ ! -d "$DOC_DIR" ]; then
    echo "❌ Documentation directory not found: $DOC_DIR"
    echo "💡 Try running the documentation setup first"
    exit 1
fi

echo "📋 Available Documentation:"
echo "=========================="

# List all documentation files
echo "1. 📖 README.md - Main documentation and quick start"
echo "2. 🔗 INTEGRATION_GUIDE.md - Rod-Corp integration architecture"
echo "3. 🛡️ EXCEPTION_HANDLING.md - Comprehensive exception management"
echo "4. 🔧 TROUBLESHOOTING.md - Problem resolution guide"
echo "5. 📊 AI_SYSTEM_TEST_REPORT.md - System validation results"
echo "6. 📚 INDEX.md - Documentation index and navigation"

echo ""
echo "🎯 Quick Access Commands:"
echo "========================"

# Quick reference commands
echo "# View main documentation"
echo "cat $DOC_DIR/README.md | head -50"

echo ""
echo "# Quick troubleshooting lookup"
echo "grep -n -A 5 -B 2 'command not found' $DOC_DIR/TROUBLESHOOTING.md"

echo ""
echo "# Search all documentation for a term"
echo "grep -r -n -i 'ollama' $DOC_DIR/"

echo ""
echo "📖 Documentation Contents Preview:"
echo "=================================="

# Show table of contents from INDEX.md
if [ -f "$DOC_DIR/INDEX.md" ]; then
    echo "📚 From INDEX.md:"
    grep -E "^#{1,3} " "$DOC_DIR/INDEX.md" | head -15
fi

echo ""

# Show quick start from README
if [ -f "$DOC_DIR/README.md" ]; then
    echo "🚀 Quick Start (from README.md):"
    sed -n '/## 🚀 Quick Start/,/## /p' "$DOC_DIR/README.md" | head -20
fi

echo ""
echo "🔍 Search Documentation:"
echo "======================="
echo "# Search for specific topics:"
echo "grep -r -n -i 'environment' $DOC_DIR/"
echo "grep -r -n -i 'database' $DOC_DIR/"
echo "grep -r -n -i 'network' $DOC_DIR/"
echo "grep -r -n -i 'model' $DOC_DIR/"

echo ""
echo "🛠️ Common Documentation Patterns:"
echo "================================="
echo "# Find all error scenarios:"
echo "grep -r -n '❌\\|Failed\\|Error' $DOC_DIR/"

echo ""
echo "# Find all solution patterns:"
echo "grep -r -n '✅\\|Solution\\|Fix' $DOC_DIR/"

echo ""
echo "# Find all commands:"
echo "grep -r -n '```bash' $DOC_DIR/ -A 3"

echo ""
echo "📁 Documentation File Sizes:"
echo "============================="
du -h "$DOC_DIR"/*.md 2>/dev/null | sort -hr

echo ""
echo "🔗 Direct File Access:"
echo "======================"
echo "# Read specific documentation:"
echo "cat $DOC_DIR/README.md"
echo "cat $DOC_DIR/TROUBLESHOOTING.md"
echo "cat $DOC_DIR/INTEGRATION_GUIDE.md"
echo "cat $DOC_DIR/EXCEPTION_HANDLING.md"

echo ""
echo "💡 Pro Tips:"
echo "============"
echo "# Open documentation in editor:"
echo "code $DOC_DIR/README.md"
echo ""
echo "# Search for specific error messages:"
echo "grep -r -n 'your error message here' $DOC_DIR/"
echo ""
echo "# View documentation structure:"
echo "tree $DOC_DIR/ 2>/dev/null || ls -la $DOC_DIR/"

echo ""
echo "🎓 Learning Path:"
echo "================="
echo "1. Start with README.md for overview"
echo "2. Check TROUBLESHOOTING.md for immediate issues"
echo "3. Review INTEGRATION_GUIDE.md for understanding"
echo "4. Study EXCEPTION_HANDLING.md for advanced topics"
echo "5. Reference INDEX.md for navigation"

# Show recent documentation updates
echo ""
echo "📅 Documentation Last Modified:"
echo "==============================="
ls -lt "$DOC_DIR"/*.md | head -6
```

This command provides comprehensive navigation and search capabilities for your AI system documentation.