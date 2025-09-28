# Tempering System Cross-Database Sampling Export (Enhanced)

## Overview
This directory contains an export of the last 10000000 datapoints for each unique_tagpath_id
aggregated across ALL databases with comprehensive TagpathMapping integration. The data includes
full name_on_hmi fields, descriptions, units, and other metadata from the TagpathMapping table.

## Export Information
- **Export Date**: 2025-07-02 00:26:21
- **Exporter Version**: 3.1 (Enhanced with Exclusion Patterns and comprehensive TagpathMapping)
- **Data Format**: CSV (Comma-Separated Values)
- **Records per Tag**: 10000000 (across all databases)
- **Total Databases**: 6
- **Export Type**: Cross-database sampling with comprehensive metadata

## Pattern Configuration
### Include Patterns Applied:
- Decorating/Temper2/Temp%

### Exclude Patterns Applied:
- decorating/temper2/temper2_upgrade%

## Enhanced Features
- **Comprehensive TagpathMapping Integration**: Full name_on_hmi, description, units, machine info
- **Enhanced Name Fallback**: Smart display name generation when name_on_hmi is missing
- **Include/Exclude Pattern Filtering**: Flexible pattern-based data selection
- **Cross-Database Aggregation**: Best records regardless of source database

## Directory Structure
```
exported_data/
├── README.md                                    # This file
├── export_summary.json                         # Overall export statistics
├── unified_sample/                             # Cross-database unified export
│   ├── tempering_unified_sample_comprehensive.csv  # Last 10000000 records with full metadata
│   ├── tagpath_mapping_unified_comprehensive.csv   # Complete TagpathMapping entries
│   └── export_metadata.json                   # Detailed metadata
└── analysis_examples/                         # Example analysis scripts
    ├── load_comprehensive_data.py             # Enhanced data loading
    ├── metadata_analysis.py                   # TagpathMapping analysis
    └── visualization_examples.py              # Enhanced plotting
```

## Data Files Description

### Unified Sample Files (Enhanced)
- **tempering_unified_sample_comprehensive.csv**: Last 10000000 records per unique_tagpath_id with full TagpathMapping metadata
- **tagpath_mapping_unified_comprehensive.csv**: Complete TagpathMapping entries (all fields) for discovered tagpaths
- **export_metadata.json**: Complete metadata and schema information with pattern details

## Enhanced Data Schema

### Comprehensive Sample Data Columns
- `tag_name`: **Enhanced display name** (name_on_hmi with smart fallback)
- `name_on_hmi`: **Original HMI name** from TagpathMapping table
- `tagpath`: **Full tagpath** for reference and filtering
- `combined_value`: **Most commonly used value** (intvalue + floatvalue)
- `timestamp_utc`: **Human-readable UTC timestamp**
- `record_rank`: **Record ranking** (1 = newest, 10000000 = oldest)
- `description`: **Tag description** from TagpathMapping
- `units`: **Units of measurement** from TagpathMapping
- `data_type`: **Data type** from TagpathMapping
- `machine`: **Machine/equipment** from TagpathMapping
- `t_stamp`: Original Unix timestamp in milliseconds
- `intvalue`: Integer component of the value
- `floatvalue`: Float component of the value
- `stringvalue`: String/text value (if applicable)
- `unique_tagpath_id`: Unique identifier for tagpath
- `database_source`: **Which database this record came from**
- `partition_name`: Database partition name

**Enhanced Benefits:**
- **Complete Metadata**: All TagpathMapping fields included
- **Smart Name Handling**: Enhanced fallback when name_on_hmi is missing
- **Pattern Flexibility**: Include and exclude patterns for precise filtering
- **Cross-Database Insights**: Full picture regardless of database boundaries
- **Rich Context**: Descriptions, units, machine info for better analysis

## Quick Start Analysis (Enhanced)

### Load Comprehensive Data
```python
import pandas as pd
from pathlib import Path

# Load comprehensive unified sample
data_file = Path('unified_sample/tempering_unified_sample_comprehensive.csv')
data = pd.read_csv(data_file)
data['timestamp_utc'] = pd.to_datetime(data['timestamp_utc'])

print(f"Loaded {len(data):,} records with comprehensive metadata")
print(f"From {data['database_source'].nunique()} databases")
print(f"Covering {data['tag_name'].nunique()} unique tags")

# Check metadata richness
hmi_names = data['name_on_hmi'].notna() & (data['name_on_hmi'] != '')
descriptions = data['description'].notna() & (data['description'] != '')
units = data['units'].notna() & (data['units'] != '')

print(f"\nMetadata availability:")
print(f"HMI names: {hmi_names.sum():,} / {len(data):,} records ({hmi_names.mean()*100:.1f}%)")
print(f"Descriptions: {descriptions.sum():,} / {len(data):,} records ({descriptions.mean()*100:.1f}%)")
print(f"Units: {units.sum():,} / {len(data):,} records ({units.mean()*100:.1f}%)")

# Current state with metadata
current_state = data[data['record_rank'] == 1]
print("\nCurrent values with metadata:")
print(current_state[['tag_name', 'name_on_hmi', 'combined_value', 'units', 'description', 'machine']].head(10))
```

### Enhanced Analysis Examples
```python
# Analyze by machine/equipment
machine_stats = data.groupby('machine')['tag_name'].nunique().sort_values(ascending=False)
print("Tags by machine:")
print(machine_stats.head(10))

# Find tags with specific units
temp_tags = data[data['units'].str.contains('°C|degC|celsius', case=False, na=False)]
print(f"\nTemperature tags found: {temp_tags['tag_name'].nunique()}")

# Quality check on name coverage
name_quality = data.groupby('tag_name').agg({
    'name_on_hmi': lambda x: (x.notna() & (x != '')).any(),
    'description': lambda x: (x.notna() & (x != '')).any(),
    'units': lambda x: (x.notna() & (x != '')).any()
})

print(f"\nName quality summary:")
print(f"Tags with HMI names: {name_quality['name_on_hmi'].sum()} / {len(name_quality)}")
print(f"Tags with descriptions: {name_quality['description'].sum()} / {len(name_quality)}")
print(f"Tags with units: {name_quality['units'].sum()} / {len(name_quality)}")
```

## Pattern Filtering Applied

### Data Inclusion Strategy
This export applies the following filtering logic:
1. **Include patterns**: Tags matching any of the include patterns are selected
2. **Exclude patterns**: Tags matching any exclude patterns are removed
3. **Final result**: Only tags that match include patterns AND don't match exclude patterns

### Example Pattern Logic
```sql
-- Equivalent SQL logic applied:
WHERE (tagpath LIKE 'Decorating/Temper2/Temp%')
  AND tagpath NOT LIKE 'decorating/temper2/temper2_upgrade%'
```

## Enhanced Use Cases

### Comprehensive System Analysis
- **Complete Context**: Full TagpathMapping metadata provides rich analysis context
- **Smart Naming**: Enhanced display names improve readability
- **Precise Filtering**: Include/exclude patterns ensure exact data selection
- **Cross-Database Insights**: Unified view regardless of database boundaries

### Quality Assurance
- **Metadata Completeness**: Check TagpathMapping data quality
- **Name Consistency**: Verify HMI naming conventions
- **Pattern Effectiveness**: Validate include/exclude pattern results

### Development and Testing
- **Sample Data**: Perfect size for development work
- **Complete Metadata**: All context needed for proper testing
- **Representative**: Recent data represents current system state

## File Format Benefits (Enhanced)
- **CSV Format**: Universal compatibility with enhanced metadata
- **Rich Context**: Comprehensive TagpathMapping fields included
- **Pattern Documentation**: Clear record of filtering applied
- **Metadata Tracking**: Full audit trail of data selection

## Support and Questions
This enhanced export provides comprehensive TagpathMapping integration. For questions about:
- **Metadata Fields**: Check tagpath_mapping_unified_comprehensive.csv for complete field definitions
- **Pattern Logic**: Review the pattern_info section in export_metadata.json
- **Name Handling**: tag_name field uses enhanced fallback logic when name_on_hmi is missing
- **Data Context**: description, units, machine fields provide additional context

## Version History
- v3.1: Enhanced with exclusion patterns and comprehensive TagpathMapping integration
- v3.0: Cross-database sampling export (database-agnostic approach)
- v2.0: Per-database last N records CSV export 
- v1.4: Bulk historical export with Parquet format
