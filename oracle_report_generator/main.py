from data_fetcher import fetch_data
from report_generator import generate_report
from data_processor import process_data

def main():
    """Main function to execute the workflow. fake update"""
    data_frame = fetch_data()
    process_data(data_frame)
    generate_report(data_frame, format='csv')

if __name__ == "__main__":
    main()
