# Implement inheritance: Employee → Manager.
class Employee:
    def __init__(self , name,salary):
        self.name = name
        self.salary = salary
    def showDetails(self):
        print(f"name:  {self.name},salary: {self.salary}" )
        
class Manager(Employee):
    def __init__(self , name , salary , department):
        super().__init__(name,salary)
        self.department = department
    def showDetails(self):
        print(f"Name: {self.name}, salary:{self.salary},department:{self.department}")
e= Employee("ALice",9000)
m = Manager("Raj",20000,"IT")
e.showDetails()
m.showDetails()
