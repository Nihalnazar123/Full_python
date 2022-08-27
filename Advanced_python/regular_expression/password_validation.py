# password  validation using basic rule and quantifiers
# rules - start with 4 upper case and end with number no limit
import  re
rule='[A-Z]{4}\d{1,}' #'[A-Z]{4}\d+
user=input('enter a password  : ')
matcher=re.fullmatch(rule,user)   #fullmatch is used in case of using if condition
if matcher is not None:
    print('valid')
else:
    print('invalid')