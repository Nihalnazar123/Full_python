l=[4,2,8,99,3,4,34,67]
new=[]
while l:
    min = l[-1]
    for i in l:
        if i<min:
            min=i
    new.append(min)
    l.remove(min)
print(new[-1])

# or
