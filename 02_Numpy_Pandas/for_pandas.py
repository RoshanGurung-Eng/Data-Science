import pandas as pd

m = pd.Series([1,2,34], index =["Ram","Shyam", "Bob"])
#print(m["Bob"])

#print(m.info())

#print(m.iloc[0])

# print(m.head(2)) # first five data from index- head
print(m.tail(2))
