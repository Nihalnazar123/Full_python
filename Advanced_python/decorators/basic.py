# decorators
# it is used to apply extra rule to a function

def valuecheck(func):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
        else:
            return func(a,b)
    return wrapper

@valuecheck   #decorator is used to avoid -ve numbers
def sub(num1,num2):
    return num1-num2
print(sub(3,6))

@valuecheck   #decorator is used to avoid fractional numbers
def div(n1,n2):
    return n1/n2
print(div(2,6))