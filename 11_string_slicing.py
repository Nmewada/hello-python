greeting = "Good Morning, "
name = "Nitin"
print(type(name))


#Concatenating two strings
c = greeting + name
print(c)

#string indexing  
print(name[4])
# name[3] = "d" --> Does not work


#string slicing
print(name[1:4])
print(name[:4]) # is same as name[0:4]
print(name[1:]) # is same as name[1:5]

#string slicing with Negative index
c = name[-4:-1] # is same is name[1:4]
print(c)


#slicing with skip value
name = "NitinIsGood"
d = name[0::1] 
print(d)

d = name[0::2] 
print(d)

d = name[0::3]
print(d)

d = name[:0:-1]
print(d)