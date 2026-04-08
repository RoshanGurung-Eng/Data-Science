# Grading system:

grade = float(input("Enter GPA:"))
if 3.6 < grade <= 4.0:
    print("A+")
elif 3.2 < grade <= 3.59:
    print("A")
elif 3.0 < grade <= 3.19:
    print("B+")
elif 2.8 < grade <= 2.99:
    print("B")
elif 2.6 < grade <= 2.79:
    print("C+")
elif 2.4 < grade <= 2.59:
    print("C")
elif 2.0 < grade <= 2.39:
    print("D")
else:
    print("Failed")

# For sum
def sum(arr):
    s = 0
    for i in arr:
        s = s + i
    print(s)
sum([1,2,3])