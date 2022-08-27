# polymorphism
# methods overloading
# in case of overloading it has same method name and different number of arguments
# it checks when the number of arguments on object creation
# in python overloading is not supported

class A:
    def setA(self,a):      #no of arguments =1
        self.a=a
        print('inside A',self.a)
class B(A):
    def setA(self):       #no of arguments =0
        print('inside B')

objB=B()
objB.setA()   #work B class method
objB.setA(3)   #work A class method