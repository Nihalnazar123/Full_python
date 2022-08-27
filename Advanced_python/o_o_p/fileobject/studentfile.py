class Student:
    def __init__(self,mark):
        self.mark=mark
    def printvalues(self):
        print(self.mark)
f=open('student.txt','r')
ma=[]
for i in f:
    data=i.rstrip('\n').split(',')
    ma.append(data[2])
max=max(ma)
s1=Student(max)
s1.printvalues()

