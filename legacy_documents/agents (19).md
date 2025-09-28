Language: Markdown
Lines of Code: 151
File: agents.md
Version: 1.0.0
Project: AI_RodChem_Crypto_Predictor
Repository: AI_RodChem_Crypto_Predictor
Author: Rod Sanchez
Created: 2024-07-12 00:00
Last Edited: 2025-07-12 04:58

# Cryptocurrency Trading System - Analysis & Restructure

## Current System Analysis

Your system is a sophisticated cryptocurrency trading pipeline with the following components:

### Data Flow Architecture
```
Binance API → Raw Data Storage → Aggregation → Technical Analysis → Signal Generation → Trading Simulation
                                                      ↓
                                              Price Prediction (LSTM)
```

### Current Files Analysis

| Current File | Purpose | Component |
|--------------|---------|-----------|
| `01_crypto.py` | Real-time data collection from Binance | Data Collection |
| `01_crypto toshiba.py` | Historical data collection | Data Collection |
| `01_crypto_mssql.py` | Database connection testing | Infrastructure |
| `00_join_csv.py` | CSV data consolidation | Data Processing |
| `03_Agregation.py` | Time interval aggregation | Data Processing |
| `02_Indexes_TA_calculations last.py` | Technical indicator calculations | Technical Analysis |
| `calculate_special_indicator.py` | TA-Lib indicator calculations | Technical Analysis |
| `04_signal_buy_sell_last hours.py` | Buy/sell signal generation | Signal Generation |
| `05_Simulation.py` | Trading simulation & backtesting | Trading Logic |
| `06_integrated.py` | Integrated data pipeline | Orchestration |
| `flaskApp.py` | LSTM price prediction model | Machine Learning |

## Proposed Repository Structure

Following your Universal AI Response Formatting Guidelines:

```
AI_CryptoTrader/
├── src/
│   ├── collectors/           # Data collection modules
│   │   ├── binance_realtime.py
│   │   ├── binance_historical.py
│   │   └── csv_consolidator.py
│   ├── processors/           # Data processing & aggregation
│   │   ├── time_aggregator.py
│   │   └── data_validator.py
│   ├── analyzers/           # Technical analysis
│   │   ├── technical_indicators.py
│   │   ├── talib_calculator.py
│   │   └── pattern_recognition.py
│   ├── signals/             # Signal generation
│   │   ├── signal_generator.py
│   │   └── signal_evaluator.py
│   ├── trading/             # Trading logic
│   │   ├── portfolio_simulator.py
│   │   └── risk_manager.py
│   ├── ml/                  # Machine learning
│   │   ├── lstm_predictor.py
│   │   └── model_trainer.py
│   ├── utils/               # Utilities
│   │   ├── database_manager.py
│   │   ├── config_loader.py
│   │   └── logger_setup.py
│   └── orchestrator/        # Main orchestration
│       ├── pipeline_manager.py
│       └── scheduler.py
├── web/
│   ├── html/
│   │   └── dashboard.html
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── charts.js
├── config/
│   ├── database.yaml
│   ├── trading_params.yaml
│   └── api_keys.env
├── data/
│   └── cache/
│       └── crypto_cache.db
├── logs/
│   └── app.log
├── docs/
│   ├── API_Documentation.md
│   ├── Installation_Guide.md
│   └── Trading_Strategy.md
└── README.md
```

## File Renaming & Organization

### Data Collection (`src/collectors/`)
- `01_crypto.py` → `binance_realtime.py`
- `01_crypto toshiba.py` → `binance_historical.py`
- `00_join_csv.py` → `csv_consolidator.py`

### Data Processing (`src/processors/`)
- `03_Agregation.py` → `time_aggregator.py`

### Technical Analysis (`src/analyzers/`)
- `02_Indexes_TA_calculations last.py` → `technical_indicators.py`
- `calculate_special_indicator.py` → `talib_calculator.py`

### Signal Generation (`src/signals/`)
- `04_signal_buy_sell_last hours.py` → `signal_generator.py`

### Trading Logic (`src/trading/`)
- `05_Simulation.py` → `portfolio_simulator.py`

### Machine Learning (`src/ml/`)
- `flaskApp.py` → `lstm_predictor.py`

### Orchestration (`src/orchestrator/`)
- `06_integrated.py` → `pipeline_manager.py`

### Infrastructure (`src/utils/`)
- `01_crypto_mssql.py` → `database_manager.py`

## Standard File Header Template

```python
# Language: Python 3.12
# Lines of Code: {calculated_lines}
# File: src/{module}/{filename}.py
# Version: 1.0.0
# Project: AI_CryptoTrader
# Repository: AI_CryptoTrader
# Author: Rod Sanchez
# Created: {YYYY-MM-DD HH:MM}
# Last Edited: {YYYY-MM-DD HH:MM}
```

## Key Improvements

### 1. Modular Architecture
- Separation of concerns with dedicated modules
- Clear data flow between components
- Easier testing and maintenance

### 2. Consistent Naming Convention
- Descriptive, action-oriented names
- Snake_case for Python files
- Clear module hierarchy

### 3. Configuration Management
- Centralized configuration in YAML files
- Environment-specific settings
- Secure API key management

### 4. Enhanced Logging
- Structured logging with proper levels
- Centralized log management
- Performance monitoring

### 5. Web Interface
- Real-time dashboard for monitoring
- Trading signal visualization
- Performance metrics display

## Database Schema Standardization

### Table Naming Convention
- `crypto_raw_data` (was `cr_01_crypto_data`)
- `crypto_aggregated_data` (was `cr_04_aggregated_data`)
- `technical_indicators` (was `cr_03_ta_results`)
- `trading_signals` (was `cr_05_signal_results`)
- `price_predictions` (existing)
- `portfolio_positions` (new)
- `trade_history` (new)

## Configuration Files

### `config/database.yaml`
```yaml
databases:
  mysql:
    host: ${MYSQL_HOST}
    user: ${MYSQL_USER}
    password: ${MYSQL_PASSWORD}
    database: ${MYSQL_ROD_CRYPTO_DB}
    pool_size: 20
    pool_recycle: 3600
  
  sqlite_cache:
    path: "data/cache/crypto_cache.db"
```

### `config/trading_params.yaml`
```yaml
trading:
  max_assets_per_hour: 50
  max_assets_per_symbol: 500
  initial_portfolio: 10000
  risk_percentage: 0.02
  
intervals:
  - "5m"
  - "15m" 
  - "30m"
  - "1h"
  - "4h"
  - "1d"

indicators:
  rsi_period: 14
  macd_fast: 12
  macd_slow: 26
  macd_signal: 9
  bb_period: 20
  bb_std: 2
```

## Next Steps

1. **Create the new repository structure**
2. **Refactor files with proper headers and naming**
3. **Implement centralized configuration**
4. **Add comprehensive logging**
5. **Create web dashboard**
6. **Add unit tests for each module**
7. **Implement proper error handling**
8. **Add API documentation**

This restructure will make your cryptocurrency trading system more maintainable, scalable, and professional while following your Universal AI Response Formatting Guidelines.