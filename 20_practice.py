#1) Write a program to store six fruits in a list entered by the user.
f1 = input("Enter Fruit Number 1: ")
f2 = input("Enter Fruit Number 2: ")
f3 = input("Enter Fruit Number 3: ")
f4 = input("Enter Fruit Number 4: ")
f5 = input("Enter Fruit Number 5: ")
f6 = input("Enter Fruit Number 6: ")
myFruitList = [f1, f2, f3, f4, f5, f6]
print(myFruitList)



#2) Write a program to accept marks of 6 students and display them in a sorted manner.
m1 = int(input("Enter Marks for Student Number 1: "))
m2 = int(input("Enter Marks for Student Number 2: "))
m3 = int(input("Enter Marks for Student Number 3: "))
m4 = int(input("Enter Marks for Student Number 4: "))
m5 = int(input("Enter Marks for Student Number 5: "))
m6 = int(input("Enter Marks for Student Number 6: "))
myList = [m1, m2, m3, m4, m5, m6]
myList.sort()
print(myList)




#3) Check that a tuple cannot be changed in Python.
a = (2,4,5,3,2)
a[0] = 45 # this will throw error




#4) Write a program to sum a list with 4 numbers.
a = [1, 4, 56, 7]
print(a[0] + a[1] + a[2] + a[3])
print(sum(a))



#5) Write a program to count the number of zeros in the following tuple:
a=(1,2,3,4)
print(a)

b=(7,2,6,0,9,0)
print(b.count(0))