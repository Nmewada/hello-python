#example one
list_1 = [1,32,4,5,45,4,4,3,3,3,5,6,3,5,6,343,343,5,4]
divide_by_3 = []
for item in list_1:
    if item%3 == 0:
        divide_by_3.append(item)
print('Without using list comprehensions', divide_by_3)
#List Comprehension
print('Using list comprehensions', [item for item in list_1 if item%3==0])






#example two
a = [3, 6, 7, 8, 9, 2, 4, 23, 75, 23, 123, 67]
# b = []
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)

# Shortcut to write the same:
b = [i for i in a if i%2==0]
print(b)
