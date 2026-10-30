"""validate.py — Schema validation and data quality checks."""
import pandas as pd

def validate_schema(df, required_columns=None, expected_types=None):
    results = {'passed': True, 'issues': [], 'stats': {}}
    if required_columns:
        missing = [c for c in required_columns if c not in df.columns]
        if missing:
            results['passed'] = False
            results['issues'].append(f"Missing columns: {missing}")
    missing_rates = (df.isnull().sum() / len(df) * 100).round(2)
    results['stats']['missing_rates'] = missing_rates.to_dict()
    results['stats']['total_rows'] = len(df)
    results['stats']['completeness_score'] = round(1 - df.isnull().mean().mean(), 4)
    n_dups = df.duplicated().sum()
    results['stats']['duplicate_rows'] = int(n_dups)
    if n_dups > 0:
        results['issues'].append(f"{n_dups} duplicate rows detected")
    if results['issues']:
        results['passed'] = False
    return results
