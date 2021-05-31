list1 = [3, 50, 2, False, 8.2, "Nitin"]

# index display
# index = 0
# for item in list1:
#     print(item, index)
#     index += 1


# The enumerate function adds counter to an iterable and returns it.
for index, item in enumerate(list1):
    print(index,item)