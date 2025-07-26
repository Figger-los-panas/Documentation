import pandas as pd
import json

def csv_to_json(csv_file, json_file):
    """
    Convert CSV file to JSON file
    """
    # Read CSV
    df = pd.read_csv(csv_file)
    
    # Convert to JSON and save
    df.to_json(json_file, orient='records', indent=2)
    
    print(f"Converted {csv_file} to {json_file}")
    print(f"Records: {len(df)}")

# Usage:
csv_to_json('optimal_combinations.csv', 'optimal_combinations.json')

# One-liner version:
# pd.read_csv('optimal_combinations.csv').to_json('optimal_combinations.json', orient='records', indent=2)