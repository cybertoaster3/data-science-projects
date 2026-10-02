# E-Commerce Purchase Behaviour Analysis

An **EDA / visualization** project exploring how Brazilians shop online using 99,000+ Olist marketplace orders. The analysis focuses on purchasing behaviour, payment methods, order value, instalments, customer reviews, and the relationship between delivery speed and satisfaction.

## Problem Statement
How do customers pay, what do they typically spend, and does delivery speed drive satisfaction? Exploratory analysis; insight + visualizations, no model.

## Dataset
- **Source**: Olist Brazilian E-commerce (data/orders.csv)
- **99,441 orders × 15 columns**: status, timestamps, n_items, price, freight, payment, installments, payment_type, review_score.

## Project Structure
```
E-Commerce Purchase Behavior Analysis/
├── 01_eda.ipynb        # Overview: structure, missing, distributions
├── 02_analysis.ipynb   # Payment methods, order value & installments, reviews, delivery→satisfaction
├── utils.py · requirements.txt · README.md
└── data/orders.csv
```

## Key Findings
All figures produced by executing the notebooks, not assumed.
- **99,441 orders, 97% delivered**; mean order **R$137.75**, mean freight **R$22.87**.
- **Credit card(76%)** is the dominant payment method, followed by **boleto (20%)**, a Brazil-specific bank slip, with voucher/debit trailing.
- **Installment culture**, about half of orders are single-payment, while remaining purchases extend across 2 to 12 monthly instalments (a core Brazilian e-commerce behaviour).
- **Customers are satisfied on average (mean review 4.09/5)**, many 5-star reviews + a chunk of 1s.
- **Slow delivery drags reviews down**, the notebook reports a correlation of -0.343 between delivery days and review score, indicating that longer delivery times are associated with lower review scores in this dataset.

## Tech Stack
- pandas, numpy, matplotlib, seaborn

## Getting Started
```bash
pip install -r requirements.txt
jupyter notebook 01_eda.ipynb
```