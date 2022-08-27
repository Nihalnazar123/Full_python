def valuecheck(func):
    def wrapper(a,b):
        if b<18:
            raise Exception('you cannot be vaccinated')
        else:
            return func(a,b)
    return wrapper

@valuecheck
def vaccian(name,age):
    return 'vaccinated successfully'

print(vaccian('nihal',12))