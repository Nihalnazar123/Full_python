# method overriding
# in case of overriding it has same method name and same number of arguments (not arguments name)
# on object creation child class will override the parent class
# it supports in python

class A:
    def printnum(self,no1):      #no of arguments =1
        self.no1=no1
        print('inside A',self.no1)
class B(A):
    def printnum(self,num1):
        self.num1=num1         #no of arguments =1
        print('inside B',self.num1)

objB=B()
objB.printnum(3)