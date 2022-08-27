# dictionary
# d={1:3,4:8,12:88}
# print(d)
# print(type(d))


#how to print keys or values only
d={'a':2,'b':4,'c':6}
u=input()
if u in d.keys():
        print(d[u])
        print(u)
else:
    print('not found')