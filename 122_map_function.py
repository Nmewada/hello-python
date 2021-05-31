#map function
#Map function takes two arguments. It takes a function name and a list
#map(function to apply,list of input)


#Without map function:
h1 = [1,2,4,5,7]
sq =[]
for item in h1:
    sq.append(item**2)
print(sq)


#With map function:
def square(n):
    return n**2

h1 = [1,2,4,5,7]
sq = list(map(square, h1))
print(sq)