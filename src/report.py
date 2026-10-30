"""report.py — Generate structured data quality reports."""
import json
from datetime import datetime

def generate_report(df, validation_results, output_path=None):
    report = {
        'generated_at': datetime.now().isoformat(),
        'dataset_summary': {'total_rows': len(df), 'total_columns': len(df.columns)},
        'validation': validation_results,
        'anomaly_summary': {},
        'recommendations': []
    }
    if 'anomaly_flag' in df.columns:
        n = int(df['anomaly_flag'].sum())
        rate = round(df['anomaly_flag'].mean() * 100, 2)
        report['anomaly_summary'] = {'total_anomalies': n, 'anomaly_rate_percent': rate, 'status': 'PASS' if rate < 5 else 'REVIEW'}
    if validation_results.get('stats', {}).get('completeness_score', 1) < 0.9:
        report['recommendations'].append("Completeness below 90% — review data collection")
    if not report['recommendations']:
        report['recommendations'].append("Dataset passed all quality checks")
    if output_path:
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2, default=str)
    return report

def print_report_summary(report):
    print("\n" + "="*50)
    print("DATA QUALITY REPORT")
    print("="*50)
    print(f"Rows: {report['dataset_summary']['total_rows']}")
    print(f"Validation: {'PASS' if report['validation']['passed'] else 'FAIL'}")
    if report['anomaly_summary']:
        print(f"Anomalies: {report['anomaly_summary']['total_anomalies']} ({report['anomaly_summary']['anomaly_rate_percent']}%)")
    for rec in report['recommendations']:
        print(f"• {rec}")
    print("="*50)
