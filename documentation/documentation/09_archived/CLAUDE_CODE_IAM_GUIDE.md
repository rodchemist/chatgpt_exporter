# Claude Code - Complete IAM & Permission Configuration Guide

## Understanding Claude Code's Permission System

### Permission Hierarchy (Highest to Lowest Priority)
1. **Enterprise policies** (`/etc/claude-code/managed-settings.json`)
2. **Command line arguments** 
3. **Local project settings** (`.claude/settings.local.json`)
4. **Shared project settings** (`.claude/settings.json`)
5. **User settings** (`~/.claude/settings.json`)

### Permission Rule Priority
- **Deny** rules > **Ask** rules > **Allow** rules

---

## Full Permission Configuration

### 1. User-Level Global Settings
File: `~/.claude/settings.json`

✅ **Created**: Contains comprehensive permissions for Python, PowerShell, development tools, file operations, and web access.

### 2. Project-Level Settings  
File: `.claude/settings.json`

✅ **Created**: Project-specific settings with broad Bash permissions, MCP server access, and additional directories.

### 3. Local Override Settings (Not in version control)
File: `.claude/settings.local.json`

✅ **Created**: Maximum permissions with `bypassPermissions` mode for trusted development.

### 4. Enterprise Policy Example
File: `~/managed-settings.json.example`

✅ **Created**: Template for system administrators with security policies and audit hooks.

---

## Permission Modes Explained

| Mode | Description | Use Case |
|------|-------------|----------|
| `default` | Prompts for permission on first use | Development with safety |
| `acceptEdits` | Auto-accepts file edits for session | Active development |
| `plan` | Analyze only, no modifications | Code review, planning |
| `bypassPermissions` | Skips ALL permission prompts | Trusted automation |

---

## Quick Setup and Usage

### Option 1: One-Command Setup
✅ **Created**: `~/setup-claude-full-permissions.sh`

```bash
./setup-claude-full-permissions.sh
```

This script automatically:
- Creates all configuration files
- Sets up convenient aliases
- Adds .gitignore entries
- Provides usage examples

### Option 2: Manual Aliases (Already Added)
✅ **Added to ~/.bashrc**:

```bash
# Full permissions - no prompts
alias claude-full='claude --defaultMode bypassPermissions'

# Python development mode  
alias claude-py='claude --defaultMode acceptEdits --allowedTools Bash,Read,Write,Edit,CreateFile'

# Safe mode - plan only
alias claude-safe='claude --defaultMode plan'

# Project mode with shared directories
alias claude-project='claude --defaultMode acceptEdits --add-dir ../shared --add-dir ../config'
```

---

## Security Features

### Permission Hook for Auditing
✅ **Created**: `~/scripts/claude-permission-hook.sh`

Features:
- Logs all tool usage to `/var/log/claude-code/tool-usage.log` (or `~/.claude/tool-usage.log`)
- Blocks dangerous commands (`rm -rf /`, `format`, `dd if=/dev/zero`)
- Requires confirmation for sensitive operations (`sudo`, `rm -rf`, `deploy`)
- Returns structured JSON responses for permission decisions

To use this hook, add to your settings:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command", 
            "command": "/home/rod/scripts/claude-permission-hook.sh"
          }
        ]
      }
    ]
  }
}
```

---

## Files Created

| File | Purpose | Status |
|------|---------|--------|
| `~/.claude/settings.json` | User-level global settings | ✅ Created |
| `.claude/settings.json` | Project-level settings | ✅ Created |
| `.claude/settings.local.json` | Local override settings | ✅ Created |
| `~/managed-settings.json.example` | Enterprise policy template | ✅ Created |
| `~/scripts/claude-permission-hook.sh` | Security audit hook | ✅ Created |
| `~/setup-claude-full-permissions.sh` | One-command setup script | ✅ Created |
| `~/.bashrc` | Shell aliases added | ✅ Updated |

---

## Usage Examples

### Maximum Permissions (No Prompts)
```bash
claude-full -p "Install all dependencies and run tests"
```

### Python Development Mode
```bash
claude-py -p "Set up virtual environment and install requirements"
```

### Safe Planning Mode
```bash
claude-safe -p "Analyze the codebase and suggest improvements"
```

### Project Mode with Shared Access
```bash
claude-project -p "Refactor the shared library modules"
```

### Direct Command Line
```bash
# Bypass all permissions
claude --defaultMode bypassPermissions -p "any command"

# Accept all edits but confirm commands
claude --defaultMode acceptEdits -p "refactor this code"

# Add additional directories
claude --add-dir ~/another-project --defaultMode acceptEdits -p "work on both projects"
```

---

## Interactive Session Commands

During a Claude Code session, you can use:

```bash
# Check current permissions
/permissions

# Add directory access
/add-dir ~/another-project

# Change permission mode
/set defaultMode bypassPermissions

# View current settings
/settings
```

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Still getting prompts | Use `claude-full` alias or `--defaultMode bypassPermissions` |
| Permission denied | Check deny rules in settings hierarchy |
| Can't access directory | Use `--add-dir` or add to `additionalDirectories` |
| MCP tools not working | Use exact format: `mcp__servername` |
| Settings not applying | Check file locations and JSON syntax |

### Debug Commands

```bash
# Test with maximum permissions
claude-full --verbose -p "test command"

# Check settings hierarchy
echo "User settings:" && cat ~/.claude/settings.json
echo "Project settings:" && cat .claude/settings.json  
echo "Local settings:" && cat .claude/settings.local.json
```

---

## Best Practices

1. **Development**: Use `claude-py` for Python work, `claude-project` for general development
2. **Automation**: Use `claude-full` only in trusted environments
3. **Production**: Always use `claude-safe` first, then apply changes
4. **Security**: Implement permission hooks for logging and compliance
5. **Version Control**: Commit `.claude/settings.json`, ignore `.claude/settings.local.json`

---

## Summary

✅ **Complete IAM & Permission Configuration Implemented**

- **No prompts** for Python/pip/PowerShell commands
- **Automatic file editing** approval
- **Full directory access** as configured
- **MCP server integration** with permissions
- **Enterprise policy** support
- **Security hooks** for auditing
- **Convenient aliases** for different use cases
- **One-command setup** script available

**Quick Start**: Run `./setup-claude-full-permissions.sh` then use `claude-full -p "your command"` for immediate full access.