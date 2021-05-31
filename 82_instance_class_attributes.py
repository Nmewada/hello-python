class Employee:
    company = "Google"
    salary = 100

nitin = Employee()
hardik = Employee()

# Creating instance attribute salary for both the objects
# nitin.salary = 300
# hardik.salary = 400
nitin.salary = 45
print(nitin.salary)
print(hardik.salary)

# Below line throws an error as address is not present in instance/class 
# print(hardik.address) 