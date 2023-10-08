import pandas as pd

df = pd.DataFrame({'name': ['Adam', 'Brian', 'Christos', 'Dolly', 'Elena', 'Dolly', 'Brian'],
                   'surname': ['Brown', 'Smith', 'Andreou', 'Brown', 'Blake', 'Andreou', 'Smith'],
                   'age': [23, 45, 12, 22, 73, 34, 45],
                   'favourite_colour': pd.Categorical(['blue', 'red', 'green', 'yellow', 'pink', 'yellow', 'red'])})

if __name__ == '__main__':
    print('Describe: ')
    print(df.describe(percentiles=None, include='all'))
    print('\n---------------\n')
    print('Info:')
    print(df.info(verbose=True, memory_usage=True))
    print('\n---------------\n')
    print('Surname value counts:')
    print(df.value_counts(subset='surname'))
    print('\n---------------\n')
    print('Shape:')
    print(df.shape)
    print('\n---------------\n')
    print('Variance:')
    print(df.var(numeric_only=True))
    print('\n---------------\n')
    print('Covariance:')
    print(df.cov(numeric_only=True))
