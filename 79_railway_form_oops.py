class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

nitinApplication = RailwayForm()
nitinApplication.name = "Nitin"
nitinApplication.train = "Rajdhani Express"
nitinApplication.printData()