# a = 12
# b = 34
# print("The sum of a and b is ", a+b)

#oops
class Number:
    def sum(self):
        return self.a + self.b

num = Number()
num.a = 12
num.b = 34
s = num.sum()
print(s)


'''
PascalCase 
classes ->EmployeeName -->PascalCase 

camelCase
isNumeric, isFloatOrInt -->camelCase
'''