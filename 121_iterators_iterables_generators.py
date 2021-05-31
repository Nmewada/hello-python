'''
iterable--object __iter or __get -iterable can give iterator
Iterator----iterator object define next method
iteration---fetch value
on the spot value generate
'''

def gen(n):
    for i in range(n):
        yield i
print(gen(1000))


 #object initialize
 # #no memory allocate
ob1=gen(4)
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))



num="nitin" 
for i in num:
    print(i)



s="sandip"
item=iter(s)
print(next(item))