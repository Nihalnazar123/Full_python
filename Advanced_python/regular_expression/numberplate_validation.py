# number plate validation using basic rule and quantifiers
import  re
rule='[K][L]\d{2}[A-Z]\d{4}'
user=input('enter a number plate  : ')
matcher=re.fullmatch(rule,user)   #fullmatch is used in case of using if condition
if matcher is not None:
    print('valid')
else:
    print('invalid')