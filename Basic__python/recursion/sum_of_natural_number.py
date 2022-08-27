def sumn(n):
    if n==0:
        return 0
    else:
        return n+sumn(n-1) #3+sumn(2)
                           #   2+sumn(1)
                            #     1+sumn(0)


print(sumn(3))