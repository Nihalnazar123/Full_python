def valuecheck(func):
    def wrapper(a,b):
        if a=='admin':
            return func(a,b)
        else:
            raise Exception('not available')
    return wrapper


@valuecheck
def changepin(user,pin):
    newpin=pin
    return newpin

print(changepin('admin',3457))
print(changepin('nihal',155367))