import requests
import pandas as pd

from io import StringIO


def download_csv_with_retries(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return pd.read_csv(StringIO(response.text))
            else:
                print(f"Attempt {attempt + 1} failed with status code {response.status_code}. Retrying...")
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed with error: {e}. Retrying...")
    raise Exception("Failed to download CSV after multiple attempts")


def merge_dataframes(df1, df2, column):
    # YOUR CODE


def filter_dataframe_by_license(df, licenses):
    # YOUR CODE


def count_imports(df, column):
    # YOUR CODE


if __name__ == "__main__":
    # Read the two CSV files
    licenses_df = pd.read_csv('licenses.csv')

    url = 'https://raw.githubusercontent.com/GirZ0n/Lupa-Visualization/main/resources/' \
          'python_imports/data/import_statements_data.csv'
    import_statements_df = download_csv_with_retries(url)

    print('licenses_df and import_statements_df shapes: ')
    print(licenses_df.shape, import_statements_df.shape)

    # Merge the two DataFrames on the "project_name" column
    merged_df = merge_dataframes(import_statements_df, licenses_df, 'project_name')

    # Filter the merged DataFrame to only include projects with the specified licenses
    permissive_licenses = ['Apache License 2.0', 'MIT License']
    filtered_df = filter_dataframe_by_license(merged_df, permissive_licenses)

    # Count the number of imports of different libraries for projects under the specified licenses
    library_import_counts = count_imports(filtered_df, 'import')
    print('library_import_counts.head(): ')
    print(library_import_counts.head())
