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
