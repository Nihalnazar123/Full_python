import re
rule='^a[\d]{5}[b]$'
user=input('enter a password  : ')
matcher=re.fullmatch(rule,user)   #fullmatch is used in case of using if condition
if matcher is not None:
    print('valid')
else:
    print('invalid')
