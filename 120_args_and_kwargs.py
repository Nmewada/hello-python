# *args and **kwargs tutorial
# *vars and **kvars tutorial


# from typing import ItemsView


def function_1(name,age,rollno):
    print("the student name is ",name,"age is ",age,"roll no is ",rollno)

function_1("Nitin", 26, 22)






def function_1(*args):
    print(type(args))
    #print("the student name is ",args[0],"age is ",args[1],"roll no is ",args[2])
    if(len(args)==3):
        print("the student name is ",args[0],"age is ",args[1],"roll no is ",args[2])
    else:
        print("the student name is ",args[0],"age is ",args[1])



#function_1("Nitin", 26, 22)
function_1("Nitin", 26)


lis=['rahul',20,100]
function_1(*lis)


def getmarks(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)
    

marklist={"nitin":100,"rahul":90,"hardik":80}
getmarks(**marklist)