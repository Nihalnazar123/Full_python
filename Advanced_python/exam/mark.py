class Person:
    def __init__(self,details):
        self.details=details
    def printvalues(self):
        print(self.details)
f = open('mark.txt', 'r')
mark = []
for i in f:
    d = i.strip('\n').split(',')
    mark.append(d[3])
    maximum = max(mark)
    if maximum <= d[3]:
        details=i
        s1=Person(details)
        s1.printvalues()