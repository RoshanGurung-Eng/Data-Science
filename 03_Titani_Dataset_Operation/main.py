import pandas as pd

d = pd.read_csv("Titanic-Dataset.csv")

#print(d.to_string())

#print(d.head())
#print(d.describe())


# Data Cleaning
new_df = d["Age"].fillna(d["Age"].median()) # Age one of the important coloumn
print(new_df)