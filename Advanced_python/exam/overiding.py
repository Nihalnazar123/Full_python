# method overriding
# in case of overriding it has same method name and same number of arguments (not arguments name)
# on object creation child class will override the parent class

class Books:
    def bookdeatils(self,name):
        self.name=name
        print(self.name)
class Booknum(Books):
    def bookdeatils(self,type):
        self.type=type
        print(self.type)
b1=Booknum()
b1.bookdeatils('action')