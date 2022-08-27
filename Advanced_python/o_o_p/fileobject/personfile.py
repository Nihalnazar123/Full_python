class Person:
    def __init__(self,name,place,age):
        self.name=name
        self.age=age
        self.place=place
    def printvalues(self):
        print(self.name)
        print(self.age)
        print(self.place)
f=open('persondata.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    name=data[0]
    place=data[1]
    age=data[2]
    p1=Person(name,place,age)
    p1.printvalues()
    print('................')