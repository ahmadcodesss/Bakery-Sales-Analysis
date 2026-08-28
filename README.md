# Bakery Sales Analysis

A Python-based data analysis project exploring sales patterns from a bakery's transaction dataset — including hourly income trends, daily trends, and product popularity.

> This project was completed as part of a Coursera data analytics course assignment, adapted and extended for portfolio purposes.

## Overview

This project analyzes point-of-sale data to answer key business questions:
- What are the busiest hours of the day?
- How does income vary by day of the week?
- Which products sell the most?

## Tools Used

- **Python 3**
- **pandas** — data loading and aggregation
- **matplotlib** — data visualization
- **openpyxl** — Excel file handling

## Data

This project expects a `bakery.xlsx` file (not included in this repository) containing transaction-level sales data with columns such as `datetime`, `hour`, `day of week`, and `total`. Place your own copy of the file in the project root before running the scripts.

## Setup

1. Clone the repository
```bash
git clone https://github.com/your-username/bakery-sales-analysis.git
cd bakery-sales-analysis
```

2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

```bash
python hourly_sales.py
python daily_sales.py
```

## Key Findings

- Sales are concentrated between **11 AM and 5 PM**, with negligible activity outside these hours.
- The bakery is closed on **Tuesdays**, reflected by a sharp drop in income that day compared to the rest of the week.

