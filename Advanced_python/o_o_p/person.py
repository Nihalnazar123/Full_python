# details of a person program
class Person:
    def persondeatils(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printdeatils(self):   #instance variable is used to point to the current instance
        print(self.name)
        print(self.age)
        print(self.place)

person1=Person()
person1.persondeatils('nihal',21,'thrissur')
person1.printdeatils()

person2=Person()
person2.persondeatils('albin',21,'mala')
person2.printdeatils()
