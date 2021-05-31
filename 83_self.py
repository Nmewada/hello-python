class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

nitin = Employee()
nitin.salary = 100000
nitin.getSalary() # Employee.getSalary(nitin)