# variables in function
# they r two types
# local and global

# local variable- it can be only accessed to a private function
# eg:
# def printx():
#     x=8
#     print(x)
# printx()
# print(x)

# global variable can be accessed from any where in function
# syntax: global variable name
def printx():
    global x
    x=8
    print(x)
printx()
print(x)