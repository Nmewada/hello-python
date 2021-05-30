# Write a program to greet all the person names stored in a list l1 and which starts with S.
# l1 = ["Nitin", "Hardik", "Sandip", "Rahul"]

l1 = ["Nitin", "Hardik", "Sandip", "Rahul", "Swapnali"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)