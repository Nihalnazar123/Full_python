f=open('filedata.txt', 'r')
l=[]
for i in f:
    d = i.rstrip('\n').split(' ')
    l.extend(d)   #extend is used to add multiple objects to list
print(l)