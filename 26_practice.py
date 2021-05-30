#1)Write a program to create a dictionary of Hindi words with values as their English translation. Provide the user with an option to look it up!
myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Options are ", myDict.keys())
a = input("Enter the Hindi Word\n")
# print("The meaning of your word is:", myDict[a])
# Below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))





#2)Write a program to input eight numbers from the user and display all the unique numbers (once).
n1=int(input("Enter number 1 : \n"))
n2=int(input("Enter number 2 : \n"))
n3=int(input("Enter number 3 : \n"))
n4=int(input("Enter number 4 : \n"))
n5=int(input("Enter number 5 : \n"))
n6=int(input("Enter number 6 : \n"))
n7=int(input("Enter number 7 : \n"))
n8=int(input("Enter number 8 : \n"))
a={n1,n2,n3,n4,n5,n6,n7,n8}
print(a)



#3)Can we have a set with 18(int) and “18”(str) as a value in it?
#start code
a={18,'18'}
print(a)
#end code


#extra info start
b={18,'18',18.0}
print(a)

a={18,'18',18.1}
print(a)
#extra info end



#4)What will be the length of the following set S:
# s = Set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# What will be the length of S after the above operations?
s=set()
s.add(20)
s.add("20")
s.add(20.0)
print(len(s))



#5)S = {}, what is the type of S?
s={}
print(type(s)) #dictionary




#6)Create an empty dictionary. Allow 4 friends to enter their favorite language as values and use keys as their names. Assume that the names are unique.
favLang = {}
a = input("Enter your favorite language Mayur\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Hardik\n")
d = input("Enter your favorite language Rahul\n")
favLang['mayur'] = a
favLang['ankit'] = b
favLang['hardik'] = c
favLang['rahul'] = d
print(favLang)


#7)If names of 2 friends are same; what will happen to the program in Program 6?
favLang = {}
a = input("Enter your favorite language Mayur\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Hardik\n")
d = input("Enter your favorite language Rahul\n")
favLang['mayur'] = a
favLang['rahul'] = b
favLang['hardik'] = c
favLang['rahul'] = d
print(favLang)



#8)If languages of two friends are same; what will happen to the program in Program 6?



#9)Can you change the values inside a list which is contained in set S
#S = {8, 7, 12, "Harry", [1, 2]}
s = {8, 7, 12, "Harry", [1, 2]} #----->this will throw error wrong we can't add list to sets...also we can't change set value
print(s)
