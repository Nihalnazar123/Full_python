
# method1
# def check():
#     n=int(input('enter a number '))
#     if n>0:
#         print('it is +ve')
#     elif n==0:
#         print('zero')
#     else:
#         print('it is -ve')
# check()


# method2
# def check(n):
#     if n>0:
#         print('it is +ve')
#     elif n==0:
#         print('zero')
#     else:
#         print('it is -ve')
# check(5)
# check(-3)
# check(0)




# method3
def check(n):
    if n>0:
        return 'positive'
    elif n==0:
        return 'zero'
    else:
        return 'negative'
print(check(-2))
print(check(4))
print(check(0))