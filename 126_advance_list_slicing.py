# Basic List Slicing:s
list1 = [11,24,32,45,75,68,38,87]
print(list1[2:7])



# Negative list slicing:
list1 = [11,24,32,45,75,68,38,87]
print(list1[-3:7])


list1 = [11,24,32,45,75,68,38,87]
print(list1[-3:])


list1 = [11,24,32,45,75,68,38,87]
print(list1[:-2])
print(list1[:6])


# Double Colon List Slicing:
list1 = [1,2,3,4,5,61,71,8,9,90]
print(list1[::2])


list2 = [1,2,3,4,5,61,71,8,9,90]
print(list2[::3])




list1 = [1,2,3,4,5,61,6,7,0,9,8,90,81]
print(list1[1:10:3])

list2 = [1,2,3,4,5,61,6,7,0,9,8,90,81]
print(list2[5:12:2])



# Reversing a list:
list1 = [1,2,3,4,5,61,6,7,0,9,8,90,81]
print(list1[::-1])

list2 = [1,2,3,4,5,61,6,7,0,9,8,90,81]
print(list2[::-2])