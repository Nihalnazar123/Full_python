class Student:
    def studentdetails(self,name,rollno,mark,dept):
        self.name=name
        self.rollno=rollno
        self.mark=mark
        self.dept=dept
    def printstudent(self):
        print('student name :',self.name)
        print(self.rollno)
        print(self.dept)
        print(self.mark)

stu1=Student()
stu1.studentdetails('nihal',27,75,'BCA')
stu1.printstudent()

stu2=Student()
stu2.studentdetails('jowsha',17,85,'BCA')
stu2.printstudent()

stu3=Student()
stu3.studentdetails('albin',22,70,'BCA')
stu3.printstudent()

