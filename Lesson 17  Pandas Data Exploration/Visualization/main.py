import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({'name': ['Adam', 'Brian', 'Christos', 'Dolly', 'Elena', 'Dolly', 'Brian'],
                   'surname': ['Brown', 'Smith', 'Andreou', 'Brown', 'Blake', 'Andreou', 'Smith'],
                   'age': [23, 45, 12, 22, 73, 34, 45],
                   'height': [178, 183, 150, 163, 158, 178, 167],
                   'favourite_colour': pd.Categorical(['blue', 'red', 'green', 'yellow', 'pink', 'yellow', 'red'])})

if __name__ == "__main__":
    # Note: use matplotlib to print plots in python scripts

    # Create a bar plot of age by favourite colour
    df.plot(x='favourite_colour', y='age', kind='bar', title='Bar plot age by fav. colour')
    plt.show()

    # Create a scatter plot of age against height
    df.plot(x='age', y='height', kind='scatter', title='Scatter plot age vs height')
    plt.show()

    # Create a histogram of the distribution of ages
    df['age'].plot(kind='hist', title='Age distribution (hist)')
    plt.show()

    # Create a Kernel Density Estimate plot of height
    df['height'].plot(kind='kde', title='Height distribution (kde)')
    plt.show()
