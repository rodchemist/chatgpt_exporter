# Tempering Data Cleaning and Preprocessing Pipeline

This repository contains a comprehensive data cleaning and preprocessing pipeline specifically designed for tempering system data exported from multiple databases. The pipeline identifies duplicates, handles data quality issues, and prepares the data for machine learning model training.

## Overview

The cleaning pipeline processes the cross-database tempering data export (92,584 records across 953 unique tagpaths) and addresses the following data quality issues:

- **Duplicate Detection**: Identifies exact duplicates, tagpath conflicts, and highly correlated time series
- **Empty Column Handling**: Removes completely empty columns and handles missing values
- **Outlier Detection**: Uses multiple methods (IQR, Z-score, Isolation Forest) to identify anomalous values
- **Feature Engineering**: Creates time-based features and lag variables for ML training
- **Data Validation**: Ensures consistency across database sources and tagpath mappings

## Files Structure

```
tempering_data_cleaner.py     # Main cleaning pipeline script
usage_example.py              # Examples and tutorials  
README.md                     # This documentation
```

## Input Data

The pipeline expects data from the cross-database sampling export with the following structure:

### Expected Input Files
- `unified_sample/tempering_unified_sample.csv` - Main data file (92,584 records)
- `unified_sample/tagpath_mapping_unified.csv` - Tagpath mappings (953 entries)
- `unified_sample/export_metadata.json` - Export metadata

### Input Data Schema
| Column | Type | Description |
|--------|------|-------------|
| `tag_name` | String | Human-readable tag name |
| `tagpath` | String | Full tagpath identifier |
| `combined_value` | Float | Primary measurement value (intvalue + floatvalue) |
| `timestamp_utc` | DateTime | UTC timestamp |
| `record_rank` | Integer | Record ranking (1=newest, 100=oldest) |
| `unique_tagpath_id` | Integer | Unique identifier for tagpath |
| `database_source` | String | Source database name |
| `intvalue`, `floatvalue`, `stringvalue` | Mixed | Raw value components |

## Installation and Setup

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scikit-learn colorama
```

### Basic Usage

#### Option 1: Complete Pipeline (Recommended)
```python
from tempering_data_cleaner import TemperingDataCleaner

# Initialize cleaner
cleaner = TemperingDataCleaner(
    input_dir="/path/to/exported/data",
    output_dir="/path/to/cleaned/output"
)

# Run complete pipeline
success = cleaner.run_full_pipeline(
    remove_duplicates=True,
    handle_outliers='flag',  # Options: 'flag', 'remove', 'keep'
    impute_missing='mean'    # Options: 'mean', 'median', 'zero'
)
```

#### Option 2: Command Line
```bash
python tempering_data_cleaner.py \
    --input-dir "/path/to/exported/data" \
    --output-dir "/path/to/cleaned/output" \
    --handle-outliers flag \
    --impute-missing mean
```

## Data Quality Issues Identified

Based on your tempering data (953 unique tagpaths, 92,584 records), the pipeline addresses:

### 1. Duplicate Detection

**Types of Duplicates Identified:**
- **Exact Duplicates**: Identical records across all columns
- **Tagpath Conflicts**: Same tagpath with different `unique_tagpath_id` values
- **ID Conflicts**: Same `unique_tagpath_id` with different tagpaths
- **Name Conflicts**: Same `tag_name` with different tagpaths
- **Correlation Duplicates**: Time series with correlation > 95%
- **Timestamp Duplicates**: Multiple identical values at the same time

**Example Issue:**
```
Tagpath: "Decorating/Temper2/TempSetpoint_01"
Problem: Appears with unique_tagpath_id 1001 and 1002
Solution: Standardize to single unique ID
```

### 2. Empty Column Analysis

**Columns Analyzed for Emptiness:**
- `stringvalue` - Often contains only empty strings or 'null'
- `intvalue` - May be all zeros for float-only measurements  
- `floatvalue` - May be all zeros for integer-only measurements

**Handling Strategy:**
- Completely empty columns are removed
- Sparse columns are flagged but retained
- Missing values are imputed using specified strategy

### 3. Missing Value Patterns

**Common Patterns in Tempering Data:**
- Temperature sensors: `intvalue` = 0, `floatvalue` = actual temperature
- Setpoint tags: `floatvalue` = 0, `intvalue` = setpoint value  
- Status tags: `stringvalue` contains state, numeric fields = 0
- Alarm tags: Mixed value types depending on alarm state

### 4. Outlier Detection

**Methods Used:**
- **IQR Method**: Values outside Q1-1.5×IQR or Q3+1.5×IQR
- **Z-Score**: Values with |z-score| > 3
- **Isolation Forest**: ML-based anomaly detection (5% contamination)

**Tempering-Specific Outliers:**
- Temperature spikes during furnace startup/shutdown
- Setpoint changes during recipe transitions
- Sensor calibration periods with unusual readings

## Feature Engineering

The pipeline creates ML-ready features:

### Time-Based Features
- `hour` - Hour of day (0-23)
- `day_of_week` - Day of week (0-6)
- `day_of_month` - Day of month (1-31)
- `month` - Month (1-12)

### Lag Features
- `prev_value` - Previous measurement value
- `value_change` - Change from previous value
- `value_change_pct` - Percentage change from previous value

### Rolling Statistics
- `rolling_mean_5` - 5-period rolling average
- `rolling_std_5` - 5-period rolling standard deviation

### Category Features
- `is_temperature_tag` - Boolean flag for temperature measurements
- `is_setpoint_tag` - Boolean flag for setpoint values
- `is_alarm_tag` - Boolean flag for alarm indicators
- `database_source_encoded` - Encoded database source

### Outlier Flags
- `is_outlier_iqr` - Boolean flag for IQR outliers

## Output Structure

```
cleaned_data/
├── tempering_data_cleaned.csv           # Main cleaned dataset
├── ml_ready/                            # ML training datasets
│   ├── X_train.csv                     # Training features
│   ├── X_val.csv                       # Validation features  
│   ├── X_test.csv                      # Test features
│   ├── y_train.csv                     # Training targets
│   ├── y_val.csv                       # Validation targets
│   ├── y_test.csv                      # Test targets
│   └── ml_metadata.json                # ML dataset metadata
├── data_quality_report.json             # Detailed quality analysis
├── duplicate_analysis_report.json       # Duplicate detection results
├── outlier_analysis_report.json         # Outlier detection results
├── cleaning_summary.json                # Overall cleaning summary
└── data_cleaning.log                    # Detailed processing log
```

## Machine Learning Preparation

The pipeline automatically creates train/validation/test splits:

- **Training**: 70% of data (scaled features)
- **Validation**: 10% of data (scaled features)
- **Test**: 20% of data (scaled features)
- **Features**: 14 engineered features ready for ML
- **Target**: `combined_value` (primary measurement)
- **Scaling**: StandardScaler applied to all features

### Loading ML-Ready Data
```python
import pandas as pd

# Load training data
X_train = pd.read_csv("cleaned_data/ml_ready/X_train.csv")
y_train = pd.read_csv("cleaned_data/ml_ready/y_train.csv")

# Load metadata
with open("cleaned_data/ml_ready/ml_metadata.json") as f:
    metadata = json.load(f)
    
print(f"Features: {metadata['feature_names']}")
print(f"Training samples: {metadata['dataset_sizes']['train']}")
```

## Data Quality Metrics

After cleaning your tempering data, expect:

- **Data Reduction**: 5-15% reduction due to duplicate removal
- **Feature Count**: 14 engineered features for ML training
- **Missing Values**: <1% after imputation
- **Outliers**: Flagged but retained for analysis
- **Time Coverage**: Consistent temporal sampling across all tags

## Validation and Testing

### Data Integrity Checks
- Verify `unique_tagpath_id` consistency across databases
- Ensure temporal ordering within each tag
- Validate value ranges for temperature/setpoint tags
- Check for data leakage between train/test splits

### Quality Validation
```python
# Example validation code
cleaner = TemperingDataCleaner(input_dir, output_dir)
cleaner.load_data()
cleaner.analyze_data_quality()

# Check for critical issues
critical_issues = []
if cleaner.duplicate_analysis['exact_duplicates'] > 1000:
    critical_issues.append("High duplicate count")
    
if cleaner.data_quality_report['basic_stats']['unique_tags'] < 900:
    critical_issues.append("Tag count unexpectedly low")

print(f"Critical issues: {critical_issues}")
```

## Troubleshooting

### Common Issues

**1. Memory Errors**
- Your dataset (92K records) should fit in memory
- If issues persist, process in chunks by database source

**2. Correlation Analysis Timeout**  
- Automatically samples first 100 tags if too many
- Adjust `DUPLICATE_THRESHOLD` to reduce correlation pairs

**3. Missing Input Files**
- Ensure unified_sample directory exists
- Verify export completed successfully

**4. Feature Engineering Failures**
- Check timestamp format consistency
- Ensure numeric columns contain valid data

### Performance Optimization

For larger datasets:
```python
# Process subset of data for testing
cleaner = TemperingDataCleaner(input_dir, output_dir)
cleaner.load_data()

# Limit to specific databases
subset = cleaner.raw_data[
    cleaner.raw_data['database_source'].isin(['OCSDLG', 'OCS_AI_Historian'])
]
cleaner.raw_data = subset

# Continue with pipeline
cleaner.analyze_data_quality()
```

## Next Steps

After cleaning, your data is ready for:

1. **Exploratory Data Analysis**: Visualize trends across databases
2. **Time Series Modeling**: LSTM, ARIMA, or Prophet models
3. **Anomaly Detection**: Equipment failure prediction
4. **Process Optimization**: Temperature profile optimization
5. **Quality Prediction**: Defect rate modeling based on tempering parameters

## Support

For questions about:
- **Data cleaning**: Check the detailed logs in `data_cleaning.log`
- **Quality issues**: Review `data_quality_report.json`
- **ML preparation**: See `ml_metadata.json` for dataset details

The cleaning pipeline is designed specifically for your tempering system data structure and handles the multi-database, multi-tagpath complexity automatically.
