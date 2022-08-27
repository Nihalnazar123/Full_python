# it is used to access single value through reference

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)
p1=Person('nihal',21,'kochi')
print(p1.name)
print(p1.place)
print(p1.age)