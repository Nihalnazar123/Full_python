class Person:
    def persondetails(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Child:
    def childdetails(self,phn,address,std):
        self.phn=phn
        self.address=address
        self.std=std
class Student(Person,Child):
    def studentdetails(self,roll,school):
        self.roll=roll
        self.school=school
    def print(self):
        print('name: ',self.name)
        print('age: ',self.age)
        print('place: ',self.place)
        print('phn: ',self.phn)
        print('address: ',self.address)
        print('std: ',self.std)
        print('roll: ',self.roll)
        print('school: ',self.school)
s1=Student()
s1.persondetails('nihal',21,'kochi')
s1.childdetails(7561899947,'kochi,kakkanad','+2')
s1.studentdetails(27,'adtjtd')
s1.print()


# using constructor
class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Child:
    def __init__(self,phn,address,std):
        self.phn=phn
        self.address=address
        self.std=std
class Student(Person,Child):
    def __init__(self,roll,school,name,age,place,phn,address,std):
        Person.__init__(self,name,age,place)
        Child.__init__(self,phn,address,std)
        self.roll=roll
        self.school=school
    def print(self):
        print('name: ',self.name)
        print('age: ',self.age)
        print('place: ',self.place)
        print('phn: ',self.phn)
        print('address: ',self.address)
        print('std: ',self.std)
        print('roll: ',self.roll)
        print('school: ',self.school)
s1=Student(27,'al azhar','nihal',21,'kochi',7561899947,'kochi,kakkand','10')
s1.print()