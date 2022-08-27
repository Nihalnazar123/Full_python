# decision making
# ---------------=
# it is divided into 3 types
# *if - if is a keyword, syntax - if num>5:
#                                     print('hello')
#
# *if else - syntax - if num>5:
#                          print('hello')
#                     else:
#                        print('no hello for u')
#
# *if elif else
# to slove intentation error use tab button

# if
num=int(input('enter a number : '))
if num>5:
    print('hello')

# if else
num=int(input('enter a number : '))
if num>5:
    print('hello')
else:
    print('no hello for u')


# nested if
# ----------
a=7
b=4
if a>0:
    if b>5:
        print('hi')
    else:
        print('hello')
else:
    print('hello hi')