students=[('anu',67),('amal',69),('arun',65)]
mark=[]
for i in students:
    mark.append(i[1])
max=(max(mark))
for i in students:
    if i[1]==max:
        print(i[0])