class Employee:
    company = "Google"
    salary = 100

nitin = Employee()
hardik = Employee()
nitin.salary = 500
hardik.salary = 400

print(nitin.company)
print(hardik.company)
Employee.company = "YouTube"
print(nitin.company)
print(hardik.company)
print(nitin.salary)
print(hardik.salary)