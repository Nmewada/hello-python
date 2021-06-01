sample_list1 = ["share", "this", "blog", "and", "subscribe", "codewithharry"]
for i in sample_list1:
    print(i, end=" ")


sample_list1 = ["share", "this", "blog", "and", "subscribe", "codewithharry"]
print(" ".join(sample_list1))


sample_list2 = ["chalk", "duster", "board", "chair", "table", "benches"]
print("We need", end=" ")
for i in sample_list2:
    print(f"{i},", end=" ")
print("in class.")


sample_list2 = ["chalk", "duster", "board", "chair", "table", "benches"]
print("We need", ", ".join(sample_list2), "in class.")


print(",".join("python"))
print(" and ".join("python"))