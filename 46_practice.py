# Write a program to print the multiplication table of a given number using for loop.

num = int(input("Enter the number"))
for i in range(1, 11):
    # print(str(num) + " X " + str(i) + "=" + str(i*num))
    print(f"{num}X{i}={num*i}") #f string




# Write a program to print the multiplication table of a given number using for loop reverse order.

num = int(input("Enter the number"))
for i in range(10, 0,-1):
    # print(str(num) + " X " + str(i) + "=" + str(i*num))
    print(f"{num}X{i}={num*i}") #f string