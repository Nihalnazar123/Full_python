data=[('anu',21),('amal',27),('mega',35),('rahul',48),('arun',42),('amala',45)]
d=[]
for i in data:
    d.append(i[1])
age=max(d)
for j in data:
    if j[1]==age:
        print(j[0])




