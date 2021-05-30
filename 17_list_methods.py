#sort method 
l1=[1,4,6,8,10,12,25,20,10]
l1.sort() 
print(l1)


#reverse method 
l1=[1,4,6,8,10,12,25,20,10]
l1.reverse()  
print(l1)


#append method
l1=[1,4,6,8,10,12,25,20,10]
l1.append(50) 
print(l1)


#insert method
l1=[1,4,6,8,10,12,25,20,10]
l1.insert(0,50)   #insert expected 2 arguments -->This will add 50 at 0 index
print(l1)


#pop method
l1=[1,4,6,8,10,12,25,20,10]
l1.pop(3)         #It will delete element at index 3 and return its value
print(l1)


#remove method
l1=[1,4,6,8,10,12,25,20,10]
l1.remove(12)     #It will remove 12 from the list
print(l1)