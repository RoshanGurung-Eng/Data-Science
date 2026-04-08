import numpy as np 

"""student_marks = [1,2,3]

print(type(student_marks))"""
n = np.array([1,2,3], dtype = str) # numpy ko wrapper
print(type(n))
print(n)

print(np.ones((3,4),dtype = int))

# np.save("mynparray",n)

f = np.array([1,2,3])
s = np.array([4,5,6])
print(np.add(f,s))

print(np.sin(f))