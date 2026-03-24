import pandas as pd 

df = pd.read_csv("Titanic-Dataset.csv")
"""
print("First five of the table:")
print(df.head()) # First five of the table
print("Last five of the table:")
print(df.tail()) # Last five of the table
print("Information about the table:")
print(df.info()) # Information about the table
print("Description of the table:")
print(df.describe()) # Description of the table"""

#Data Cleaning
new_df = df["Age"].fillna(df['Age'].median(),inplace=True)
print(new_df) # After cleaning the data and filling the missing values with the median of the column
print(df.info()) # Information about the table

print(df.drop(columns=['Cabin','Ticket'], inplace=True)) # Dropping the columns 'Cabin' and 'Ticket' from the table
print(df.info()) # Information about the table

df["Sex"] = df["Sex"].map({"male":0,"female":1})
print(df["Sex"])

print(df.rename(columns={'Sex': 'Gender'})) # Renaming the column 'Sex' to 'Gender'
print(df.info()) # Information about the table