'''
syntax:
lambda argument:manipulate(argument)
'''

#without lamda function
def add(a, b):
    s = a+b
    return s
print(add(4,12))

#wit lamda function
# lambda argument : condition/output
add = lambda x,y:x+y
print(add(4,12))



#without lamda function
def x(val):
    return val[1]
a = [(1,2), (4,5), (555,3)]
a.sort(key=x)
print(a)


#with lamda function
a = [(1,2), (4,5), (555,3)]
a.sort(key=lambda x:x[1])
print(a)