# AI System Backup and Restore

Backup and restore AI agent configurations, with options for emergency recovery.

## Usage
This command manages your AI system configuration backups and provides emergency restoration options.

## Implementation
```bash
echo "💾 AI System Backup and Restore Manager"
echo "======================================="

# Function to show backup status
show_backup_status() {
    echo "📋 Current Backup Status:"
    echo "========================="

    local backup_dir="$HOME/.bashrc_backups"
    if [ -d "$backup_dir" ]; then
        echo "📁 Backup directory: $backup_dir"
        echo "📊 Total backups: $(ls -1 "$backup_dir"/*.bak 2>/dev/null | wc -l)"

        echo ""
        echo "📅 Recent backups:"
        ls -lt "$backup_dir"/*.bak 2>/dev/null | head -5 | while read line; do
            echo "  $line"
        done

        echo ""
        echo "💽 Disk usage: $(du -sh "$backup_dir" 2>/dev/null | cut -f1)"
    else
        echo "❌ Backup directory not found: $backup_dir"
    fi
}

# Function to create backup
create_backup() {
    local backup_type="${1:-manual}"
    echo "💾 Creating $backup_type backup..."

    if [ -x "/home/rod/.local/bin/backup-bashrc" ]; then
        /home/rod/.local/bin/backup-bashrc "$backup_type"
    else
        echo "❌ Backup script not found. Creating manual backup..."
        local timestamp=$(date '+%Y%m%d_%H%M%S')
        local backup_file="$HOME/.bashrc_backups/bashrc_${backup_type}_${timestamp}.bak"
        mkdir -p "$HOME/.bashrc_backups"
        cp "$HOME/.bashrc" "$backup_file" && echo "✅ Manual backup created: $backup_file"
    fi
}

# Function to restore from backup
restore_backup() {
    local backup_dir="$HOME/.bashrc_backups"

    echo "🔄 Available backups for restoration:"
    echo "====================================="

    if [ ! -d "$backup_dir" ] || [ ! "$(ls -A "$backup_dir"/*.bak 2>/dev/null)" ]; then
        echo "❌ No backups found in $backup_dir"
        return 1
    fi

    local backups=($(ls -t "$backup_dir"/*.bak 2>/dev/null))
    for i in "${!backups[@]}"; do
        local backup_file="${backups[$i]}"
        local backup_name=$(basename "$backup_file" .bak)
        local backup_date=$(stat -c %y "$backup_file" 2>/dev/null | cut -d' ' -f1,2 | cut -d: -f1,2)
        echo "$((i+1)). $backup_name ($backup_date)"
    done

    echo ""
    echo "💡 To restore a backup:"
    echo "   cp $backup_dir/[backup_file] ~/.bashrc"
    echo "   source ~/.bashrc"
    echo ""
    echo "🚨 Emergency restore (latest manual backup):"
    local latest_manual=$(ls -t "$backup_dir"/bashrc_manual_*.bak 2>/dev/null | head -1)
    if [ -n "$latest_manual" ]; then
        echo "   cp '$latest_manual' ~/.bashrc && source ~/.bashrc"
    else
        local latest_any=$(ls -t "$backup_dir"/*.bak 2>/dev/null | head -1)
        if [ -n "$latest_any" ]; then
            echo "   cp '$latest_any' ~/.bashrc && source ~/.bashrc"
        fi
    fi
}

# Function to emergency restore
emergency_restore() {
    echo "🚨 Emergency System Restore"
    echo "==========================="

    local backup_dir="$HOME/.bashrc_backups"
    local latest_backup=$(ls -t "$backup_dir"/*.bak 2>/dev/null | head -1)

    if [ -n "$latest_backup" ]; then
        echo "🔄 Restoring from: $(basename "$latest_backup")"

        # Create emergency backup of current state
        local emergency_backup="$backup_dir/bashrc_emergency_$(date '+%Y%m%d_%H%M%S').bak"
        cp "$HOME/.bashrc" "$emergency_backup"
        echo "💾 Current state backed up to: $emergency_backup"

        # Restore from backup
        cp "$latest_backup" "$HOME/.bashrc"
        echo "✅ Configuration restored from backup"

        # Reload configuration
        source "$HOME/.bashrc"
        echo "🔄 Configuration reloaded"

        # Test basic functionality
        if command -v ai-help >/dev/null 2>&1; then
            echo "✅ AI commands available after restore"
        else
            echo "⚠️  AI commands not available - may need manual intervention"
        fi
    else
        echo "❌ No backups available for emergency restore"
        echo "💡 Try manually recreating configuration or check documentation"
    fi
}

# Main menu
echo "Choose an action:"
echo "1. Show backup status"
echo "2. Create manual backup"
echo "3. Create pre-update backup"
echo "4. List available backups for restore"
echo "5. Emergency restore (latest backup)"
echo ""

# For Claude Code, we'll show all options
echo "🔍 Showing backup status:"
show_backup_status

echo ""
echo "💾 Creating manual backup:"
create_backup "manual"

echo ""
echo "📋 Available backups for restore:"
restore_backup

echo ""
echo "🛠️ Additional Commands:"
echo "========================"
echo "backup-bashrc manual          # Create manual backup"
echo "backup-bashrc pre-update      # Create pre-update backup"
echo "backup-bashrc startup         # Create startup backup"
echo ""
echo "📖 For detailed backup documentation:"
echo "cat /home/rod/rod-corp/docs/ai-agents/README.md | grep -A 20 'Backup System'"
```

This command provides comprehensive backup and restore capabilities for your AI system configuration.