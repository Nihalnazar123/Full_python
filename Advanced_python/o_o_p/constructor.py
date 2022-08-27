# constructor
# it is used to initialize instance variable at the time of object creation

class Person:
    def __init__(this,name,age,location):
        this.name=name
        this.age=age
        this.location=location

    def printvalue(this):
        print(this.name)
        print(this.age)
        print(this.location)


p1=Person('anu',23,'kochi')
p1.printvalue()