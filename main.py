def main():
    print("Hello from data-science!")


if __name__ == "__main__":
    main()


grade = float(input("Enter Grade:"))
if 3.8 < grade <= 4.0:
    print("A")
elif 3.6 < grade < 3.8:
    print("A-")
else:
    print("Below A")
print(type(grade))


def sum(a):
    b = a
    s = 0
    for i in b:
        s = s + i
    print(s)

sum([4,8,3])


def adder(nums):
    sum = 0
    for i in nums:
        sum += i #sum = sum + i 
    print ("Sum is : "+str(sum))

adder([1,2,3])
