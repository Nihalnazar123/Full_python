class Person:
    def persondetails(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Phone:
    def phonedetails(self,phn):
        self.phn=phn
class Student(Person):
    def studentdetails(self,rollno,school):
        self.roll=rollno
        self.school=school
class Teacher(Student,Phone):
    def teacherdeatils(self,dept,salary):
        self.dep=dept
        self.salary=salary
    def print(self):
        print(self.name)
        print(self.age)
        print(self.place)
        print(self.school)
        print(self.dep)
        print(self.salary)
        print(self.phn)

t1=Teacher()
t1.persondetails('nihal',21,'kochi')
t1.studentdetails(27,'al azhar')
t1.teacherdeatils('science',25000)
t1.phonedetails(7561899947)
t1.print()