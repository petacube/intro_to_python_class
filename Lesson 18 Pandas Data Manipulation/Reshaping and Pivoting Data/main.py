import pandas as pd

data = {
    "Gender": ["M", "M", "F", "F", "M", "F", "M"],
    "AgeGroup": ["18-30", "18-30", "18-30", "31-50", "31-50", "31-50", "18-30"],
    "Purchased": [1, 0, 1, 1, 0, 1, 1],
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Creating a cross-tabulation
cross_tab = pd.crosstab(index=df["Gender"], columns=df["AgeGroup"], values=df["Purchased"], aggfunc="sum")

print("\nCross-tabulation:")
print(cross_tab)
