n=input('enter a element ')
s='luminar'
b=''
for i in s:
    if i in n:
        continue
    else:
        b=b+i
        print(i,end='')