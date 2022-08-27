# multiple_inheritance
# when child class has more than one parent it is called multiple inheritance

# 1.multiple inheritance
class A:  #parent class/super class/base class
    def seta(self,num1):
        self.num1=num1
        print('inside A class',self.num1)
class B:   #parent class
    def setb(self):
        print('inside B class')
class C(A,B):    #child class/sub class/derived class
    def setc(self):
        print('inside C class',self.num1)
c1=C()
c1.seta(2)
c1.setb()
c1.setc()
