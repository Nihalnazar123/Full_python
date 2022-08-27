class Students:
    dep='bca'
    clg='asmabi'
    def __init__(self,name,roll,place):
        self.name=name
        self.roll=roll
        self.place=place
    def printvalues(self):
        print(self.name)
        print(self.roll)
        print(self.place)
        print(Students.dep)
        print(Students.clg)

st1=Students('nihal',21,'kochi')
st1.printvalues()
