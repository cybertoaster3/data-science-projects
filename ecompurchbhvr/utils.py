"""
E-Commerce Purchase Behaviour Analysis - Utility Functions for EDA project (no model)
Loads the dataset and provides light helpers; the analysis lives in the notebooks
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_dataset(filepath="data/orders.csv"):
    return pd.read_csv(filepath, low_memory=False)

def missing_report(df):
    """missing counts and percentages per column, starting from worst"""
    m = df.isnull().sum()
    out = pd.DataFrame({"missing": m, "pct": (100*m/len(df)).round(2)})
    return out[out["missing"] > 0].sort_values("missing", ascending=False)

def top_counts(series, n=10, sep=None):
    """Value counts (optionally splitting multi-value cells on 'sep')"""
    s = series.dropna()
    if sep:
        s = s.str.split(sep).explolde().str.strip()
    return s.value_counts().head(n)