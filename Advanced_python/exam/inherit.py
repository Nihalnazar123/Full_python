class Vehicle:
    def valuecheck(self,name,type):
        self.name=name
        self.type=type


class Bus(Vehicle):
    def busvalue(self,company,price):
        self.company=company
        self.price=price

    def printvalue(self):
        print('name of the vehicle', self.name)
        print('type of the vehicle', self.type)
        print('company of the vehicle', self.company)
        print('price of the vehicle',self.price)

b1=Bus()
b1.valuecheck('bus','fourwheel')
b1.busvalue('tata',2000000)
b1.printvalue()

