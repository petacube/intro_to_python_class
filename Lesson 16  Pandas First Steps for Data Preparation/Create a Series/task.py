import pandas as pd


def create_series(dict_: dict):
    # TODO


if __name__ == "__main__":
    students = ["Alice", "Bob", "Charlie", "David"]
    name_lengths_dict = {name: len(name) for name in students}
    series = create_series(name_lengths_dict)
    print(series)
