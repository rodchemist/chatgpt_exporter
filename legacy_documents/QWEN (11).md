# Qwen Context Documentation - Manufacturing Visualization Dashboard

## Project Overview
This repository contains a manufacturing dashboard visualization project with 12 different charts implemented using Chart.js v4. The dashboard provides real-time insights into manufacturing operations, quality metrics, and financial performance.

## Directory Structure
```
manufacturing_plots/
├── index.html     # Main HTML structure and layout
├── style.css      # Styling and theme definitions
└── main.js        # Chart implementations and data visualization logic
```

## Key Components

### index.html
- HTML5 document structure for the dashboard
- Responsive layout with CSS Grid
- 12 different chart containers organized in 5 sections:
  1. Quick KPIs (4 cards)
  2. Operations (5 charts)
  3. Quality & Mix (3 charts)
  4. Performance & Risk (3 charts)
  5. Financials (1 mixed chart)
- Uses Chart.js CDN for visualization library
- Responsive design with mobile-friendly grid adjustments

### style.css
- Dark theme styling with CSS variables for consistent color scheme
- Responsive grid layouts (1200px breakpoint)
- Custom styling for cards, headers, and typography
- Color palette defined in `:root` variables:
  - Background: #0f1222
  - Panel: #171a2f
  - Accents: Teal (#4dd0e1), Purple (#7c4dff), Orange (#ffb74d), Red (#ef5350), Green (#66bb6a)

### main.js
- Implementation of all 12 charts using Chart.js v4
- Dynamic theme integration with CSS variables
- Utility functions for data generation and formatting
- Custom Chart.js plugin for center text in doughnut charts
- Chart types implemented:
  1. Line chart (Production Trend)
  2. Bar chart (Orders per Month)
  3. Semi-doughnut gauge (Utilization)
  4. Doughnut chart (Downtime Causes)
  5. Stacked bar chart (Returns by Reason)
  6. Radar chart (Quality KPIs)
  7. Polar area chart (Product Share)
  8. Horizontal bar chart (Top Defect Types)
  9. Scatter plot (Temp vs Vibration)
  10. Bubble chart (Defect Severity)
  11. Area line chart (Energy)
  12. Mixed bar/line chart (Revenue vs Margin)

## Technical Details
- Uses Chart.js v4 for all visualizations
- Fully responsive design that adapts to different screen sizes
- Dynamic data generation with random values for demonstration
- Custom theming that integrates with Chart.js options
- Single-page application with no external dependencies besides Chart.js