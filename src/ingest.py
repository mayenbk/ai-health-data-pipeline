"""ingest.py — Data ingestion from CSV files and REST APIs."""
import requests
import pandas as pd

def load_from_csv(filepath, encoding='utf-8'):
    df = pd.read_csv(filepath, encoding=encoding)
    print(f"Loaded {len(df)} rows, {len(df.columns)} columns")
    return df

def load_from_api(url, params=None, timeout=15):
    response = requests.get(url, params=params, timeout=timeout)
    response.raise_for_status()
    data = response.json()
    if isinstance(data, list) and len(data) == 2:
        return pd.DataFrame(data[1]) if data[1] else pd.DataFrame()
    if isinstance(data, list):
        return pd.DataFrame(data)
    for key in ['data', 'results', 'records']:
        if key in data:
            return pd.DataFrame(data[key])
    return pd.DataFrame([data])
