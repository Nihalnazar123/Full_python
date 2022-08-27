# phone number validation using basic rule and quantifiers
import  re
rule='[0-9]{10}'
user=input('enter a number : ')
matcher=re.fullmatch(rule,user)   #fullmatch is used in case of using if condition
if matcher is not None:
    print('valid')
else:
    print('invalid')