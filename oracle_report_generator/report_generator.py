import pandas as pd

def generate_report(df, format='csv'):
    """Generate a report in the specified format."""
    if df is not None and not df.empty:
        if format == 'csv':
            report_file = "employee_report.csv"
            df.to_csv(report_file, index=False)
            print(f"CSV report generated: {report_file}")
        elif format == 'json':
            report_file = "employee_report.json"
            df.to_json(report_file, orient='records', lines=True)
            print(f"JSON report generated: {report_file}")
    else:
        print("No data available to generate report.")
 
