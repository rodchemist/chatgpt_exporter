# Tempering Data Testing Usage Guide

## Overview

This guide shows you how to comprehensively test your tempering data export using the provided testing tools. The testing suite includes three main components:

1. **Main Test Suite** (`tempering_test_suite.py`) - Comprehensive data validation
2. **Data Validator** (`tempering_data_validator.py`) - Specialized tempering data validation
3. **Integration Tester** (`analysis_integration_tester.py`) - Tests analysis examples

## Prerequisites

Make sure you have the required Python packages installed:

```bash
pip install pandas numpy matplotlib seaborn pyarrow tabulate colorama
```

## Quick Start Testing

### 1. Basic Export Validation

First, run the main test suite to validate your export structure and data quality:

```bash
python tempering_test_suite.py --export-dir /path/to/your/export/directory
```

**What it tests:**
- Export directory structure
- Data schema consistency
- Data quality and completeness
- TagpathMapping coverage
- Loading performance
- Analysis readiness

**Example output:**
```
TEMPERING DATA EXPORT TEST SUITE
================================
Testing directory: /mnt/d/00_Working_area/tempering
Found 3 database exports to test

✓ Structure check for OCSHDK
✓ Schema validation for OCSHDK  
✓ Data quality for OCSHDK
✓ TagpathMapping coverage for OCSHDK: 98.5%

OVERALL TEST RESULT: PASS
```

### 2. Tempering-Specific Validation

Run the specialized tempering data validator for detailed analysis:

```bash
python tempering_data_validator.py --export-dir /path/to/export --database OCSHDK
```

**What it validates:**
- Tempering pattern matching
- Data integrity checks
- Specialized tempering metrics
- Data exploration and profiling
- Performance benchmarking
- Quick visualizations

**Example output:**
```
TEMPERING DATA VALIDATION - OCSHDK
==================================

✓ Pattern 'setpoints/09_tu%' found (45 unique tagpaths, 1,234,567 records)
✓ Pattern '%Decorating/Temper2%' found (23 unique tagpaths, 567,890 records)
✓ Tempering data percentage: 78.5%
✓ Temperature range check: 2.1% extreme values

Validation complete!
```

### 3. Analysis Integration Testing

Test that the generated analysis examples work correctly:

```bash
python analysis_integration_tester.py --export-dir /path/to/export
```

**What it tests:**
- Analysis example scripts exist
- Data loading functions work
- Basic analysis runs successfully
- Visualizations generate correctly
- Documentation is complete

## Detailed Testing Workflows

### Workflow 1: Complete Export Validation

```bash
# Step 1: Run comprehensive test suite
python tempering_test_suite.py --export-dir /your/export/dir --log-level INFO

# Step 2: Check specific databases
python tempering_data_validator.py --export-dir /your/export/dir --database OCSHDK
python tempering_data_validator.py --export-dir /your/export/dir --database OCS_AI_Historian

# Step 3: Test analysis integration
python analysis_integration_tester.py --export-dir /your/export/dir

# Step 4: Review test reports
ls /your/export/dir/*test*report*.json
```

### Workflow 2: Pattern-Specific Testing

If you used custom patterns in your export, test them specifically:

```bash
python tempering_data_validator.py \
  --export-dir /your/export/dir \
  --database OCSHDK \
  --patterns "your_custom_pattern%" "another_pattern%"
```

### Workflow 3: Performance Testing Focus

For performance-focused testing:

```bash
# Run main suite with debug logging for detailed performance info
python tempering_test_suite.py \
  --export-dir /your/export/dir \
  --log-level DEBUG

# Then run validator for benchmarking
python tempering_data_validator.py --export-dir /your/export/dir --database OCSHDK
```

## Understanding Test Results

### Test Reports Generated

Each test creates detailed JSON reports:

1. **`test_report.json`** - Main test suite results
2. **`{database}_validation_report.json`** - Database-specific validation
3. **`integration_test_report.json`** - Analysis integration results
4. **`test_results.log`** - Detailed logging

### Key Metrics to Watch

**Data Quality Indicators:**
- Schema match rate: Should be 100%
- TagpathMapping coverage: Should be >95%
- Data integrity score: Should be >80%
- Pattern coverage: Should match your expectations

**Performance Indicators:**
- Loading time: <5 seconds for typical files
- Query performance: <2 seconds for basic operations
- Memory usage: Reasonable for your system

**Integration Indicators:**
- All analysis examples should work
- Visualizations should generate successfully
- Documentation should be complete

## Troubleshooting Common Issues

### Issue: "No database exports found"

**Problem:** Test can't find your exported data
**Solution:** 
```bash
# Check directory structure
ls -la /your/export/dir/
# Should see directories like: OCSHDK_export, OCS_AI_Historian_export
```

### Issue: "Schema validation failed"

**Problem:** Data columns don't match expected schema
**Solution:** Check export script completed successfully and all data files are present

### Issue: "TagpathMapping coverage low"

**Problem:** Many unique_tagpath_ids in data don't have mappings
**Solution:** 
- Verify OCS_AI database connection during export
- Check TagpathMapping table completeness
- Review export patterns

### Issue: "Analysis examples don't work"

**Problem:** Generated analysis scripts fail
**Solution:**
```bash
# Test manually
cd /your/export/dir
python -c "
import sys
sys.path.append('analysis_examples')
import load_data
print(load_data.get_available_databases('.'))
"
```

## Advanced Testing

### Custom Test Scripts

You can create custom tests by importing the test classes:

```python
from tempering_test_suite import TemperingDataTester
from tempering_data_validator import TemperingDataValidator

# Custom testing
tester = TemperingDataTester('/your/export/dir')
databases = tester.discover_exports()

# Run specific tests
for db in databases:
    validator = TemperingDataValidator('/your/export/dir')
    results = validator.run_full_validation(db['name'])
```

### Automated Testing Pipeline

Create a complete testing pipeline:

```bash
#!/bin/bash
# complete_test_pipeline.sh

EXPORT_DIR="/your/export/directory"

echo "=== Running Complete Tempering Data Test Pipeline ==="

# Step 1: Main validation
echo "Step 1: Main Test Suite"
python tempering_test_suite.py --export-dir "$EXPORT_DIR" --log-level INFO

# Step 2: Database-specific validation  
echo "Step 2: Database-Specific Validation"
for db in OCSHDK OCS_AI_Historian OCS_AI_short_history; do
    if [ -d "$EXPORT_DIR/${db}_export" ]; then
        echo "Testing database: $db"
        python tempering_data_validator.py --export-dir "$EXPORT_DIR" --database "$db"
    fi
done

# Step 3: Integration testing
echo "Step 3: Integration Testing"
python analysis_integration_tester.py --export-dir "$EXPORT_DIR"

# Step 4: Generate summary
echo "Step 4: Test Summary"
echo "Test reports generated:"
ls -la "$EXPORT_DIR"/*test*report*.json

echo "=== Testing Pipeline Complete ==="
```

## Test Automation

### Setting Up Automated Testing

For continuous validation, you can set up automated testing:

```python
# automated_testing.py
import schedule
import time
from pathlib import Path

def run_daily_tests():
    """Run daily validation tests"""
    export_dir = Path("/your/export/dir")
    
    # Run main test suite
    os.system(f"python tempering_test_suite.py --export-dir {export_dir}")
    
    # Email results or log to monitoring system
    # ... your notification logic here

# Schedule daily tests
schedule.every().day.at("02:00").do(run_daily_tests)

while True:
    schedule.run_pending()
    time.sleep(60)
```

## Best Practices

1. **Run tests immediately after export** to catch issues early
2. **Save test reports** for historical tracking  
3. **Monitor performance trends** over time
4. **Test with different data patterns** to ensure robustness
5. **Validate on different environments** if deploying to multiple systems

## Integration with CI/CD

For automated environments, use exit codes:

```bash
# In your CI/CD pipeline
python tempering_test_suite.py --export-dir /data/tempering
if [ $? -eq 0 ]; then
    echo "Tests passed - deploying data"
    # Deploy or process data
else
    echo "Tests failed - check logs"
    exit 1
fi
```

## Getting Help

If tests fail or you need help interpreting results:

1. Check the detailed log files (*.log)
2. Review the JSON test reports
3. Look at the generated visualizations in `validation_plots/`
4. Check the analysis examples in `analysis_examples/`

The testing suite is designed to be comprehensive but easy to use. Start with the basic workflow and gradually use more advanced features as needed.