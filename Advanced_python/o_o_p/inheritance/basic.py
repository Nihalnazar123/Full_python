# inheritance
# it is used to get methods of one to an another class



# 1.single inheritance
# child class only has one parent class is know as single inheritance
class A:  #parent class/super class/base class
    def seta(self,num1):
        self.num1=num1
        print('inside A class',self.num1)
class B(A):   #child class/sub class/derived class
    def setb(self):
        print('inside B class',self.num1)
a1=A()
a1.seta(21)
b1=B()
b1.seta(21)
b1.setb()