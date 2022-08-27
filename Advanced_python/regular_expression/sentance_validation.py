# string start with a
# end with b

# aaaab   ajejdhec1257b   ab  a122323@#$b


# import  re
# rule='^a[\w\W]*b$'
# user=input('enter a password  : ')
# matcher=re.fullmatch(rule,user)   #fullmatch is used in case of using if condition
# if matcher is not None:
#     print('valid')
# else:
#     print('invalid')



# slove rule: special charaters and numbers can occur exactly 5 times
# import re
# rule='[\W\d]{5}'
# user=input('enter a password  : ')
# matcher=re.fullmatch(rule,user)   #fullmatch is used in case of using if condition
# if matcher is not None:
#     print('valid')
# else:
#     print('invalid')



# slove rule: only upper case and lower case letters can occur min 3 max 7
# import re
# rule='[a-zA-z]{3,7}'
# user=input('enter a password  : ')
# matcher=re.fullmatch(rule,user)   #fullmatch is used in case of using if condition
# if matcher is not None:
#     print('valid')
# else:
#     print('invalid')


# slove rule: start with number and end with number letters andspecial charaters and numbers can occur exactly 4 times
# import re
# rule='^\d[\w\W]{2}\d$'
# user=input('enter a password  : ')
# matcher=re.fullmatch(rule,user)   #fullmatch is used in case of using if condition
# if matcher is not None:
#     print('valid')
# else:
#     print('invalid')


import re
rule='^[\d\W][A-Z]{3,8}[\d\W]$'
user=input('enter a password  : ')
matcher=re.fullmatch(rule,user)   #fullmatch is used in case of using if condition
if matcher is not None:
    print('valid')
else:
    print('invalid')
