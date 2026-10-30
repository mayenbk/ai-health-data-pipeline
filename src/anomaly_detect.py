"""anomaly_detect.py — ML-based anomaly detection using Isolation Forest."""
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

def detect_anomalies(df, numeric_columns=None, contamination=0.05, random_state=42):
    df = df.copy()
    if numeric_columns is None:
        numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    if not numeric_columns:
        df['anomaly_flag'] = 0
        df['anomaly_score'] = 0
        return df
    X = df[numeric_columns].fillna(df[numeric_columns].median())
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    iso = IsolationForest(contamination=contamination, random_state=random_state, n_estimators=100)
    predictions = iso.fit_predict(X_scaled)
    scores = iso.score_samples(X_scaled)
    df['anomaly_flag'] = (predictions == -1).astype(int)
    df['anomaly_score'] = np.round(-scores, 4)
    print(f"Detected {df['anomaly_flag'].sum()} anomalies ({round(df['anomaly_flag'].mean()*100, 2)}%)")
    return df
