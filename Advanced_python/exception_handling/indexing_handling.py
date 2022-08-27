# another example for exception_handling

l=[1,2,3]
i=int(input('enter a number '))
try:
    print(l[i])
except:
    print('invalid index')
finally:
    print('always execute')

# we can find the error occurred using except exception - method
# l=[1,2,3]
# i=int(input('enter a number '))
# try:
#     print(l[i])
# except Exception as e:
#     print(e)