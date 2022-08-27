# finally block execute whether the condition is true or not
l=[1,2,3]
i=int(input('enter a number '))
try:
    print(l[i])
except:
    print('invalid index')
finally:
    print('always execute')