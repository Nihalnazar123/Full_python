def valid(func):
    def wrapper(a):
        rule = '[+][9][1][\d]{10}'
        import re
        mathcer=re.fullmatch(rule,a)
        if mathcer is not None:
                return func(a)
        else:
            raise Exception('not valid')
    return wrapper
@valid
def change_number(phn_number):
    new_number=phn_number
    return new_number
print(change_number('+911294567890'))