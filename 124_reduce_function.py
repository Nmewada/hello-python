from functools import reduce

def string_sum(a, b):
    return a+b

newstring = reduce(string_sum, ["You", " are", " with", " Nitin"])
print(newstring)



def sum_num(a, b):
    return a+b

li = reduce(sum_num, [1,2,3,4])
print(li)