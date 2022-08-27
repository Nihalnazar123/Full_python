class Person:
    def persondetails(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Student(Person):
    dep='bca'
    clg='asmabi'
    def studentdetails(self,roll):
        self.roll=roll

    def printstudent(self):
        print(self.name)
        print(self.age)
        print(self.place)
        print(self.roll)
        print(Student.dep)
        print(Student.clg)



st1=Student()
st1.studentdetails(27)
st1.persondetails('nihal',21,'kochi')
st1.printstudent()




#  using constructor
# it is used to initialize instance variable at the time of object creation
class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Student(Person):
    dep='bca'
    clg='asmabi'
    def __init__(self,roll,name,age,place):
        super().__init__(name,age,place) #super is used to call a single parent incase of multiple parents use classname with (__init__(self,roll,name,age,place)
        self.roll=roll

    def printstudent(self):
        print(self.name)
        print(self.age)
        print(self.place)
        print(self.roll)
        print(Student.dep)
        print(Student.clg)
s1=Student(21,'nihal',27,'kochi')
s1.printstudent()