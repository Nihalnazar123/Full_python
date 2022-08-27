# to string method
# it is used to give store a value which is related to the object reference
# it can only return string values.if we want to give int values covert to string value
# in case of multiple values use + ____(self.name + self.place)______

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)
    def __str__(self):
        return self.name
p1=Person('nihal',21,'kochi')
print(p1)
p1.printvalue()
