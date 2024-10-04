def process_data(df):
    """Process the data for reporting."""
    # Example processing: Calculate average salary
    if df is not None and not df.empty:
        avg_salary = df['salary'].mean()
        print(f"The average salary of employees is: {avg_salary:.2f}")
        return avg_salary
    return None
 
