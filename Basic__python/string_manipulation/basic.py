# string_manipulation
# s='luminar technolab'
# for i in s:
#     print(i)

# check out inbuild function in string

# ....find a element in a string using string_manipulation...

# n=input('enter a string ')
# s='luminar technolab'
# for i in s:
#     if n==i:
#         print('present')
#     else:
#         print('not present')



#...... method using flag value.....

# n=input('enter a string ')
# s='luminar technolab'
# f=0
# for i in s:
#     if i==n:
#         f=1
# if f==1:
#     print('present')
# else:
#     print('not present')


# ...........method using for , break , else(important)............

# for i in  range(3):
#     if i==5:
#         break
# else:
#     print('inside else')
    # (else only work in case of if break is not true or work)

# ex:for above problem
# n=input('enter a string ')
# s='luminar technolab'
# for i in s:
#     if i==n:
#         print("present")
#         break
# else:
#     print('not present')

# .............method using if statement (it can only be used if any one of input value is single element)......
# syntax - if n in s:
#        - if n not in s:

# n=input('enter a string ')
# s='luminar technolab'
# if n in s:
#     print('present')
# else:
#     print('not present')


# logic for storeing elements in empty string
s1='luminar'
s2=''
for i in s1:
    s2=s2+i
print(s2)
