# *args -(arguments)
# it is used in case of many arguments are given
# it gives output back in form of tuple

def printdata(*args):
    print(args)
printdata(1,3,4,56,7)



# use *args for many input addition
def add(*args):
    l=0
    for i in args:
        l=l+i
    print(l)
add(1,2,3,45)