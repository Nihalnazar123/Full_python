f=open('phone_num.txt', 'r')
b=open('validphn.txt', 'w')
for i in f:
    d=i.rstrip('\n')
    if len(d)==10:
        b.write(i)