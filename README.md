# AI Powered Health Data Quality Pipeline

A production ready Python pipeline that automates ingestion, validation, cleaning, and anomaly detection of public health datasets using machine learning.

## What It Does

1. **Ingests** health data from public APIs or CSV files
2. **Validates** data quality — missing values, outliers, schema violations
3. **Cleans** and standardises the dataset automatically
4. **Detects anomalies** using Isolation Forest (ML-based)
5. **Generates** a structured data quality report

## Use Cases

- Pre-processing DHS or WHO datasets for research workflows
- Automated data readiness checks before ML model training
- Data quality auditing for health information systems
- Monitoring health indicator feeds for reporting pipelines

## Setup

```bash
git clone https://github.com/mayenbk/ai-health-data-pipeline
cd ai-health-data-pipeline
pip install -r requirements.txt
python run_pipeline.py --input data/your_data.csv
```

## Quick Start

```python
from src.ingest import load_from_csv
from src.validate import validate_schema
from src.clean import clean_dataset
from src.anomaly_detect import detect_anomalies
from src.report import generate_report, print_report_summary

df = load_from_csv('data/input.csv')
validation = validate_schema(df)
df_clean = clean_dataset(df)
df_flagged = detect_anomalies(df_clean)
report = generate_report(df_flagged, validation)
print_report_summary(report)
```

## Repository Structure

```
ai-health-data-pipeline/
├── README.md
├── requirements.txt
├── run_pipeline.py
├── config/
│   └── pipeline_config.yaml
├── src/
│   ├── ingest.py
│   ├── validate.py
│   ├── clean.py
│   ├── anomaly_detect.py
│   └── report.py
└── outputs/
    └── sample_report.json
```

## Author

**Mayen Ben-Koko**
[linkedin.com/in/mayenbk](https://linkedin.com/in/mayenbk)

## License
MIT License
