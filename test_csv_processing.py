import pandas as pd
import io

def process_csv(file_content):
    try:
        # Simulate reading from file
        df = pd.read_csv(io.StringIO(file_content))
        print("DataFrame head:")
        print(df.head())
        return df.head().to_dict(orient='records')
    except Exception as e:
        print(f"Error processing file: {e}")

# Example CSV content
csv_content = "name,age,city\nAlice,30,New York\nBob,25,Los Angeles\nCharlie,35,Chicago"
result = process_csv(csv_content)
print(result)
