f=open('name.txt', 'r')
c=''
for i in f:
    if i[0]=='a':
        c=c+i
print(c)