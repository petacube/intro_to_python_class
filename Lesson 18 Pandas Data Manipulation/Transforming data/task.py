import pandas as pd


def total_sales_per_city(df_):
    # YOUR CODE


def average_sales_per_category(df_):
    # YOUR CODE


if __name__ == "__main__":
    data = {
        "City": ["London", "London", "New York", "New York", "New York", "Tokyo", "Tokyo"],
        "Category": ["Electronics", "Clothing", "Electronics", "Electronics", "Clothing", "Electronics", "Clothing"],
        "Sales": [7000, 2000, 7000, 4000, 5000, 5000, 1000],
        "Offers": [70, 20, 10, 70, 40, 50, 50],
    }

    df = pd.DataFrame(data)

    print("Total sales per city:\n", total_sales_per_city(df))
    print("\nAverage sales per category:\n", average_sales_per_category(df))
