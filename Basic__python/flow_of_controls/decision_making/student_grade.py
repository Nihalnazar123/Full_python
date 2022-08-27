# score
# 90 to 100 A+
# 80 to 89 A
# 70 to 79 B+
# ......
# bel 50 fail
# above 100 invalid

num=int(input('enter the score of the subject : '))
if num>=90 and num<=100:         #if score>100:
    print('your grade is A+')       #print('invalid')
elif num>=80 and num<=89:         #elif score>90:
    print('your grade is A')         #print('A+')
elif num>=70 and num<=79:
    print('your grade is B+')
elif num>=60 and num<=69:
    print('your grade is B')
elif num>=50 and num<=59:
    print('your grade is C+')
elif num<50:
    print('failed')
else:
    print("invalid")
