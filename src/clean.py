"""clean.py — Automated data cleaning and standardisation."""
import pandas as pd

def clean_dataset(df, strategy='median'):
    df = df.copy()
    df.columns = [c.lower().strip().replace(' ', '_') for c in df.columns]
    n_before = len(df)
    df = df.drop_duplicates()
    if n_before - len(df) > 0:
        print(f"Removed {n_before - len(df)} duplicates")
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype in ['float64', 'int64']:
                fill = df[col].median() if strategy == 'median' else df[col].mean()
                df[col] = df[col].fillna(fill)
            else:
                mode = df[col].mode()
                if len(mode) > 0:
                    df[col] = df[col].fillna(mode[0])
    return df
