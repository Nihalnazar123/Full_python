class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Parent(Person):
    def setparent(self,phn,address):
        self.phn=phn
        self.address=address
class Employee(Parent):
    def setemployee(self,emp_id,company):
        self.emp_id=emp_id
        self.company=company
    def printvalues(self):
        print('name: ',self.name)
        print('age: ',self.age)
        print('place: ',self.place)
        print('phn: ',self.phn)
        print('address: ',self.address)
        print('emp_id: ',self.emp_id)
        print('company: ',self.company)
em1=Employee()
em1.setperson('nihal',21,'kochi')
em1.setparent(7561899947,'kochi,kakkand')
em1.setemployee(27,'luminar')
em1.printvalues()


# using constructor
class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Parent(Person):
    def __init__(self,phn,address,name,age,place):
        super().__init__(name,age,place)
        self.phn=phn
        self.address=address
class Employee(Parent):
    def __init__(self,emp_id,company,phn,address,name,age,place):
        super().__init__(phn,address,name,age,place)
        self.emp_id=emp_id
        self.company=company
    def printvalues(self):
        print('name: ',self.name)
        print('age: ',self.age)
        print('place: ',self.place)
        print('phn: ',self.phn)
        print('address: ',self.address)
        print('emp_id: ',self.emp_id)
        print('company: ',self.company)
em1=Employee(27,'luminar',7561899947,'kochi,kakkand','nihal',21,'kochi')
em1.printvalues()
