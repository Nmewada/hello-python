# Create a class programmer for storing information of a few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")


nitin = Programmer("Nitin", "GitHub")
alka = Programmer("Alka", "Skype")
nitin.getInfo()
alka.getInfo()
