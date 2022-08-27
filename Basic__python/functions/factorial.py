# method 1
# def fact():
#     n = int(input('enter a number'))
#     fact = 1
#     for i in range(1, n+1):
#         fact*=i
#     print(fact)
# fact()


# method2
# def fact(n):
#     fac=1
#     for i in range(1,n+1):
#         fac*=i
#     print(fac)
# fact(5)


# method3
def fact(n):
    fac = 1
    for i in range(1,n+1):
          fac*=i
    return fac

print(fact(5))