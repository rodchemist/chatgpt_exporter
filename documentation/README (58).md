# Claude Code Custom Commands - AI Agent System

This directory contains custom Claude Code slash commands for enhanced AI agent development and system management.

## 📋 Available Commands

### 🤖 AI System Management
- **/ai-status** - Comprehensive AI system health check with enhanced error handling
- **/ai-env** - Environment management and troubleshooting with detailed diagnostics
- **/ai-fix** - Automated troubleshooting and repair with rollback capabilities
- **/ai-backup** - Configuration backup and restore with selective options
- **/ai-debug** - Deep debugging and diagnostics with log analysis
- **/ai-agents** - Quick launcher for all AI agents with performance metrics
- **/ai-docs** - Documentation navigation and search with intelligent filtering

### 📚 Project-Specific Commands (in local `.claude/commands/`)
- **/books-ai** - Analyze AI agent books collection with knowledge extraction
- **/project-setup** - Configure project for AI development with environment validation

## 🚀 Quick Usage

In Claude Code, simply type the slash command:

```
/ai-status
/ai-agents
/books-ai
```

## 🎯 Command Categories

### System Health & Monitoring
```bash
/ai-status          # Complete system overview with performance metrics
/ai-debug           # Deep diagnostic analysis with log parsing
/ai-fix             # Auto-repair common issues with backup verification
/ai-monitor         # Continuous monitoring with alerts (NEW)
```

### Environment & Configuration
```bash
/ai-env             # Environment management with version checking
/ai-backup          # Backup and restore configs with selective restore
/ai-update          # Update system components (NEW)
/project-setup      # Setup current project with validation
```

### Development & Productivity
```bash
/ai-agents          # Launch AI agents with benchmarking
/ai-docs            # Navigate documentation with search
/ai-test            # Run system tests (NEW)
/books-ai           # Analyze research materials with insights
```

## 🔧 Command Locations

- **Global Commands:** `~/.claude/commands/` (work in any project)
- **Project Commands:** `.claude/commands/` (specific to current project)

## 📖 Enhanced Command Details

### /ai-status
Runs comprehensive health checks including:
- Network services (Rod-Corp ports) with latency metrics
- Database connectivity (MSSQL + SQLite) with performance stats
- Ollama service and models with GPU utilization
- Environment status with package version checking
- Recent system activity with resource usage
- **New:** JSON output option for programmatic use

### /ai-agents
Quick launcher showing:
- Available AI agents (cloud + local) with response time metrics
- Model status and alternatives with performance benchmarks
- Environment recommendations with compatibility checking
- Launch commands and tips with usage examples
- **New:** Agent comparison features

### /ai-fix
Automated troubleshooting:
- Reloads configurations with backup verification
- Starts services with dependency checking
- Fixes permissions with audit trail
- Tests functionality with comprehensive validation
- **New:** Interactive repair mode and rollback capabilities

### /ai-env
Environment management:
- Shows current environment with package versions
- Lists available environments with compatibility matrix
- Checks package availability with version recommendations
- Provides activation commands with dependency resolution
- **New:** Environment switching and creation wizards

### /ai-backup
Backup management:
- Shows backup status with size and date information
- Creates manual backups with selective options
- Lists restoration options with preview capabilities
- Emergency recovery with step-by-step guidance
- **New:** Automated backup scheduling

### /ai-debug
Deep diagnostics:
- System information with hardware specs
- Network connectivity with detailed tracing
- Database debugging with query analysis
- Performance metrics with bottleneck identification
- Log analysis with error pattern recognition
- **New:** Export capabilities for bug reports

### /ai-docs
Documentation navigation:
- Lists all documentation with search functionality
- Provides search commands with intelligent filtering
- Shows quick references with bookmark management
- Direct file access with offline capabilities
- **New:** Bookmark management

### /books-ai (Project-Specific)
AI books analysis:
- Lists books collection with categorization
- Provides reading recommendations with priority ranking
- Suggests study plans with learning path optimization
- Content extraction tools with knowledge synthesis
- **New:** Progress tracking and insights extraction

### /project-setup (Project-Specific)
Project configuration:
- Detects project type with framework identification
- Sets up development environment with dependency installation
- Configures Git repository with best practices
- Integrates AI agents with optimal configurations
- **New:** Template-based setup and validation

## 🛠️ Creating Custom Commands - Enhanced Guidelines

To create your own commands with improved structure and reliability:

1. **For global commands:**
   ```bash
   touch ~/.claude/commands/my-command.md
   ```

2. **For project-specific commands:**
   ```bash
   mkdir -p .claude/commands
   touch .claude/commands/my-command.md
   ```

3. **Enhanced command format with error handling:**
   ```markdown
   # Command Title

   Brief description of what the command does.

   ## Usage
   Explain how to use the command with examples.

   ## Implementation
   ```bash
   #!/bin/bash
   # Enhanced command with error handling
   
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
   
   # Error handling
   set -e
   
   # Check prerequisites
   if ! command -v required-tool >/dev/null 2>&1; then
       print_error "Required tool 'required-tool' not found"
       exit 1
   fi
   
   # Main implementation
   print_header "Executing Command"
   # Your bash commands here with proper error handling
   print_success "Command executed successfully"
   ```

   ## Options
   - `--verbose`: Enable verbose output
   - `--help`: Show help information

   ## Examples
   ```bash
   /command-name --verbose
   /command-name --help
   ```

## 🎯 Enhanced Integration with AI Agent System

These commands are specifically designed to work with the Rod-Corp AI Agent System with enhanced integration:

- **Environment Integration:** Works with mamba environments and automatic fallbacks
- **Service Integration:** Manages Rod-Corp services with health checks
- **Database Integration:** Handles MSSQL + SQLite fallbacks with connection pooling
- **Model Integration:** Manages Ollama models with automatic alternatives
- **Documentation Integration:** Links to comprehensive docs with search capabilities
- **New:** Real-time monitoring and alerting integration

## 📊 System Requirements

- Rod-Corp AI Agent System installed (v2.1+)
- Claude Code CLI (latest version)
- Bash shell environment with enhanced utilities
- Optional: Ollama for local models with GPU support
- Optional: Mamba for environment management with conda fallback
- Optional: Docker for containerized services

## 🔄 Updates and Maintenance

Commands are automatically available after creation. To update:

1. Edit the `.md` file
2. Claude Code will pick up changes automatically
3. No restart required
4. **New:** Version tracking and compatibility checking

## 💡 Best Practices and Standards

1. **Use descriptive names:** Commands should be self-explanatory and follow naming conventions
2. **Include usage examples:** Show practical use cases with expected outputs
3. **Handle errors gracefully:** Check for prerequisites and provide helpful error messages
4. **Provide helpful output:** Guide users through processes with clear progress indicators
5. **Integration-aware:** Leverage existing AI agent infrastructure with proper fallbacks
6. **Standardized formatting:** Use consistent emojis, headers, and output structure
7. **Performance considerations:** Optimize for speed and resource usage
8. **Security awareness:** Validate inputs and avoid unsafe operations

## 🆘 Troubleshooting Commands

If commands don't work:

1. **Check file location:** Ensure `.md` files are in correct directory with proper permissions
2. **Verify syntax:** Commands must follow markdown format with valid bash code
3. **Test bash code:** Ensure bash implementation works independently
4. **Check permissions:** Files should be readable and executable where needed
5. **Validate dependencies:** Ensure all required tools and libraries are available
6. **Review logs:** Check system logs for error messages and debugging information

## 📞 Support and Maintenance

For issues with these commands:
1. Run `/ai-debug` for system diagnostics with detailed log analysis
2. Check `/ai-docs` for documentation with search functionality
3. Use `/ai-fix` for automated repairs with rollback capabilities
4. Review Rod-Corp documentation in `/home/rod/rod-corp/docs/` with updated guides
5. **New:** Submit bug reports with automatic environment capture

---

**Command System Status:** 🟢 Fully Operational and Enhanced

*Custom Claude Code Commands for Rod-Corp AI Agent System v2.1*
*Enhanced with standardized error handling, improved output formatting, and new features*