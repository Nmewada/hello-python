# With statement
# The best way to open and close the file automatically is the "with" statement.
# There is no need to write f.close() as it is done automatically

with open('another.txt','r') as f:
    a=f.read()
print(a)
with open('another.txt','w') as f:
    a=f.write("yessss")
print(a)
