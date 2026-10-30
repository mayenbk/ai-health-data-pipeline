"""run_pipeline.py — Main entry point for the AI health data pipeline."""
import argparse
import yaml
from src.ingest import load_from_csv
from src.validate import validate_schema
from src.clean import clean_dataset
from src.anomaly_detect import detect_anomalies
from src.report import generate_report, print_report_summary

def run_pipeline(config_path=None, input_path=None):
    print("\n=== AI Health Data Pipeline ===\n")
    config = {}
    if config_path:
        with open(config_path) as f:
            config = yaml.safe_load(f)
    data_path = input_path or config.get('data_source', {}).get('path')
    if not data_path:
        raise ValueError("No data source specified.")
    print("[1/4] Ingesting data...")
    df = load_from_csv(data_path)
    print("[2/4] Validating schema...")
    validation = validate_schema(df, required_columns=config.get('schema', {}).get('required_columns'))
    print("[3/4] Cleaning dataset...")
    df_clean = clean_dataset(df)
    print("[4/4] Detecting anomalies...")
    df_flagged = detect_anomalies(df_clean)
    output_path = config.get('output', {}).get('report_path', 'outputs/quality_report.json')
    report = generate_report(df_flagged, validation, output_path=output_path)
    print_report_summary(report)
    return df_flagged, report

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str)
    parser.add_argument('--input', type=str)
    args = parser.parse_args()
    run_pipeline(config_path=args.config, input_path=args.input)
