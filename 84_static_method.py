class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod #static method decorator
    def time():
        print("The time is 9AM in the morning")

nitin = Employee()
nitin.salary = 100000
nitin.getSalary("Thanks!") # Employee.getSalary(nitin)
nitin.greet() # Employee.greet()
nitin.time()