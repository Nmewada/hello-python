#Generator Comprehension
    #object initialize
    #no memory allocate
    #this is time taking process
gen = (i for i in range(56) if i%3==0)
for item in gen:
    print(item)