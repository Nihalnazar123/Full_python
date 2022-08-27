# slove  student id using static variable

class Student:
    dep='BCA'
    col='mes asmabi'
    def studentid(self,name,rollno):
        self.name=name
        self.roll=rollno
    def printstudentid(self):
        print('name :',self.name)
        print('rollno: ',self.roll)
        print('dep: ',Student.dep)
        print('col: ',Student.col)
        
s1=Student()
s1.studentid('nihal',27)
s1.printstudentid()

s2=Student()
s2.studentid('rinz',34)
s2.printstudentid()