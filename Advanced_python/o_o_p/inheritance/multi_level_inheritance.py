# multi_level_inheritance

class A:  #parent class/super class/base class
    def seta(self,num1):
        self.num1=num1
        print('inside A class',self.num1)
class B(A):   #parent class and also child class
    def setb(self):
        print('inside B class',self.num1)
class C(B):    #child class/sub class/derived class
    def setc(self):
        print('inside C class',self.num1)

b1=B()
b1.seta(2)
b1.setb()
c1=C()
c1.seta(4)
c1.setb()
c1.setc()