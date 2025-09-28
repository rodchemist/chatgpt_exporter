# Bashrc Reorganization Guide

Your shell configuration has been split into focused modules so you can maintain and debug it quickly. The cleaned `.bashrc` now delegates specialized logic to companion files that live alongside the migration script.

## Files in /mnt/d/DownloadChrome
- `bashrc_clean` → drop-in replacement for `~/.bashrc`
- `ai_agents_aliases` → Claude and multi-model helpers
- `ai_enhanced_aliases` → placeholder for advanced routines
- `rod_corp_config` → Rod-Corp environment and automation
- `claude_conductor_config` → Conductor launcher
- `migrate_bashrc.sh` → backup + deploy utility (executable)
- `README_BASHRC_REORG.md` → this document

## Key Improvements
1. Removed duplicate mamba/conda blocks in favour of a single detection routine
2. Consolidated Rod-Corp variables into one file for easy rotation
3. Moved AI aliases to dedicated modules and added usage hints
4. Normalized PATH setup with a helper that prevents repeated entries
5. Added automatic WSL path translation plus tmux helpers in clean sections

## Automatic Migration (recommended)
```bash
chmod +x /mnt/d/DownloadChrome/migrate_bashrc.sh
/mnt/d/DownloadChrome/migrate_bashrc.sh
source ~/.bashrc
```
The script saves timestamped backups in `~/.bashrc_backups/` before installing the new files.

## Manual Review Option
```bash
diff -u ~/.bashrc /mnt/d/DownloadChrome/bashrc_clean | less
# Repeat for other files if desired
```
If satisfied:
```bash
cp /mnt/d/DownloadChrome/bashrc_clean ~/.bashrc
cp /mnt/d/DownloadChrome/ai_agents_aliases ~/.ai_agents_aliases
cp /mnt/d/DownloadChrome/ai_enhanced_aliases ~/.ai_enhanced_aliases
cp /mnt/d/DownloadChrome/rod_corp_config ~/.rod_corp_config
cp /mnt/d/DownloadChrome/claude_conductor_config ~/.claude_conductor_config
source ~/.bashrc
```

## Smoke Tests
After loading the new shell session run:
```bash
ai-help           # confirm AI aliases
rod-corp-status   # ensure endpoints respond
mamba --version   # verify environment manager hook
which claude      # validate CLI availability
```

## Rollback
Backups live in `~/.bashrc_backups`. To restore a saved copy:
```bash
cp ~/.bashrc_backups/.bashrc_<TIMESTAMP> ~/.bashrc
source ~/.bashrc
```
Repeat for any other file you want to roll back.

## Next Steps
- Populate `~/.ai_enhanced_aliases` with your advanced workflow once ready
- Store sensitive credentials (like Rod-Corp secrets) in a secrets manager if possible
- Version-control these modular files for easier collaboration
