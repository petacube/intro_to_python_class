import requests
import pandas as pd

from io import StringIO


def download_csv_with_retries(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=5)  # Set a reasonable timeout in seconds to avoid hanging indefinitely
            if response.status_code == 200:
                return pd.read_csv(StringIO(response.text))
            else:
                print(f"Attempt {attempt + 1} failed with status code {response.status_code}. Retrying...")
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed with error: {e}. Retrying...")
    raise Exception("Failed to download CSV after multiple attempts")


if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/jetbrains-academy/gateway-to-pandas/main/Pandas/import_stats.csv'
    # Download data from GitHub and load it into a DataFrame

    print("First 5 rows of the DataFrame:")
    # Display the first 5 rows of the DataFrame

    print("\nShape of the DataFrame:")
    # Display the shape of the DataFrame

    print("\nSummary statistics of the DataFrame:")
    print(df.describe())
