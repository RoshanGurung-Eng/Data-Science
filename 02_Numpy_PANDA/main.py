import numpy as np

a = np.array([1,2,3])
print(a)
print(type(a))

b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
print(b)

# Initial Placeholders

print(np.zeros((3,4))) 
c = np.ones((2, 3, 4), dtype=np.int16)
print(c)

np.savez( 'array.npz', a, b,c)


import pandas as pd
print(pd.__version__)

d = pd.Series([1,2,3,4,5])
print(d)

# Pandas Placeholders

df_empty = pd.DataFrame()
print("\nEmpty DataFrame:")
print(df_empty)

df_zeros = pd.DataFrame(np.zeros((3, 3)), columns=['A', 'B', 'C'])
print("\nDataFrame of Zeros:")
print(df_zeros)

df_ones = pd.DataFrame(np.ones((2, 4)), columns=['W', 'X', 'Y', 'Z'])
print("\nDataFrame of Ones:")
print(df_ones)
