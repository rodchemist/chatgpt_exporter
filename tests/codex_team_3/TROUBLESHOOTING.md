# Troubleshooting Guide

## Overview
Comprehensive troubleshooting guide for the Universal Documentation System. This guide covers common issues, diagnostic procedures, and resolution strategies.

## Installation Issues

### Issue: Python version compatibility
**Symptoms:** Import errors or module not found
**Solution:**
```bash
# Check Python version
python --version
# Ensure Python 3.8+ is installed
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: Permission errors during installation
**Symptoms:** Permission denied errors
**Solution:**
```bash
# Use virtual environment (recommended)
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Common Runtime Issues

### Issue: Documentation not generating
**Symptoms:** No documentation files created after scan
**Diagnostic:**
```bash
# Check system status
python agents/scripts/documentation_engine.py --verify

# Review scan results
python agents/scripts/documentation_engine.py --scan
```
**Solution:**
1. Check write permissions in project directory
2. Verify Python version (3.8+ required)
3. Check logs in `.documentation/logs/`
4. Ensure all required directories exist

### Issue: Database errors
**Symptoms:** SQLite errors in logs
**Diagnostic:**
```bash
# Check database file exists
ls -la .documentation/tracking.db

# Check database integrity
sqlite3 .documentation/tracking.db "PRAGMA integrity_check;"
```
**Solution:**
1. Delete `.documentation/tracking.db`
2. Re-run initialization: `python agents/scripts/documentation_engine.py --init`
3. Regenerate documentation: `python agents/scripts/documentation_engine.py --generate`

### Issue: Quality scores too low
**Symptoms:** Documentation failing quality checks
**Diagnostic:**
```bash
# Review quality metrics
python agents/scripts/documentation_engine.py --metrics
```
**Solution:**
1. Add required sections (overview, usage, installation, api, license)
2. Include code examples with triple backticks
3. Ensure minimum content length (500+ characters)
4. Remove TODO/FIXME placeholders
5. Update documentation templates in `.documentation/templates/`

## Usage Examples

### Diagnostic Commands
```bash
# Complete system verification
python agents/scripts/documentation_engine.py --verify

# Quality metrics analysis
python agents/scripts/documentation_engine.py --metrics

# Project scan for issues
python agents/scripts/documentation_engine.py --scan
```

### Log Analysis
```bash
# View recent activity logs
tail -f .documentation/logs/activity_$(date +%Y%m%d).log

# Search for errors
grep -i error .documentation/logs/*.log
```

## API Troubleshooting

### Programmatic Debugging
```python
from agents.scripts.documentation_engine import DocumentationEngine

# Initialize with debug mode
engine = DocumentationEngine()

# Check system state
verification = engine.verify_implementation()
print(f"System completeness: {verification['score']}%")

# Analyze scan results
results = engine.scan_project()
print(f"Missing docs: {results['missing_docs']}")
```

## Getting Help
- **Logs**: Check `.documentation/logs/` for detailed activity logs
- **Database**: Inspect `.documentation/tracking.db` for stored metrics
- **Templates**: Review `.documentation/templates/` for customization
- **Verification**: Run `python agents/scripts/documentation_engine.py --verify`

## License
This troubleshooting guide is part of the Universal Documentation System, released under the MIT License.

---
*Troubleshooting Guide v1.0.0*
