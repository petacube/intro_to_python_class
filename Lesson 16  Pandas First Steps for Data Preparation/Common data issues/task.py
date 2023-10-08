import pandas as pd

data = {
    'ID': [1, 2, 3, 3, 4, 5, 6, 7],
    'Name': ['Alice', 'Bob', 'Charlie', 'Charlie', 'Eve', 'Frank', None, 'Grace'],
    'Age': [25, 30, 22, 22, 28, None, 45, 32],
    'Height': [5.5, 6.1, 5.8, 5.8, None, 5.9, 6.2, '5.7'],
}

df = pd.DataFrame(data)


def drop_duplicates_id(df):
    # Remove duplicates based on the 'ID' column


def fillna(df):
    # Identify and handle missing values in the 'Age' column, replacing the gaps with the column mean


def correct_inconsistency(df):
    # Correct inconsistencies in the 'Height' column by converting all values to float


df_no_duplicates = drop_duplicates_id(df)
print("DataFrame after removing duplicates:")
print(df_no_duplicates)

df_fillna = fillna(df_no_duplicates)
print("\nDataFrame after handling missing 'Age' values:")
print(df_fillna)

print("\nDataFrame after correcting inconsistencies:")
print(correct_inconsistency(df_fillna))
