class Person:
    def persondetails(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Employee(Person):
    com='luminar'
    def employeedetails(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary
    def printemployee(self):
        print(self.name)
        print(self.age)
        print(self.place)
        print(self.emp_id)
        print(self.salary)
        print(Employee.com)
em1=Employee()
em1.persondetails('nihal',21,'kochi')
em1.employeedetails(2003,25000)
em1.printemployee()



#  using constructor
class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Employee(Person):
    com='luminar'
    def __init__(self,emp_id,salary,name,age,place):
        super().__init__(name,age,place)
        self.emp_id=emp_id
        self.salary=salary
    def printemployee(self):
        print(self.name)
        print(self.age)
        print(self.place)
        print(self.emp_id)
        print(self.salary)
        print(Employee.com)

e1=Employee(27,25000,'nihal',21,'kochi')
e1.printemployee()
