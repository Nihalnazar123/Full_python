n=input('enter a string ')
v='''!@#$%^&*()_+-={}[]:";<>,./'|'''
b=''
for i in n:
    if i not in v:
        b=b+i
print(b)
