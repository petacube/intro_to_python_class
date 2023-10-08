import pandas as pd

df = pd.DataFrame({'name': ['Adam', 'Brian', 'Christos', 'Dolly', 'Elena', 'Dolly', 'Brian'],
                   'surname': ['Brown', 'Smith', 'Andreou', 'Brown', 'Blake', 'Andreou', 'Smith'],
                   'age': [23, 45, 12, 22, 73, 34, 45],
                   'favourite_colour': pd.Categorical(['blue', 'red', 'green', 'yellow', 'pink', 'yellow', 'red'])})


def sort(df):  # return sorted df
   # TODO)


if __name__ == '__main__':
    print(sort(df))
