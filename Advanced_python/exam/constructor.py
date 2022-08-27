class Animals:
    def __init__(self,type,sex):
        self.type=type
        self.sex=sex
class Dogs(Animals):
    def __init__(self,name,breed,type,sex):
        super().__init__(type,sex)
        self.name = name
        self.breed=breed

    def print(self):
        print(self.name)
        print(self.breed)
        print(self.type)
        print(self.sex)
d1=Dogs('arjun','dog','omnivorous','M')
d1.print()
