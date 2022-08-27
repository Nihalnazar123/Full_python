f=open('data1.txt','r')
for i in f:
    d = i.split(' ')
print('total word count',len(d))
