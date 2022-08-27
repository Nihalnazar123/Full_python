# error creation

# n1=int(input('enter a number '))
# if n1<0:
#     raise Exception('negative value')
# else:
#     print(n1+10)



n1=int(input('enter a number '))
n2=int(input('enter a number '))
if n1<n2:
    raise Exception('negative value')
else:
    print(n1-n2)
