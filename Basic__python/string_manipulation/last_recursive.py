#
# n=input('enter a string ')
# s=''
# s1=''
# for i in n:
#     if i not in s:
#         s=s+i
#     else:
#         s1=s1+i
# print(s1)

n=input('enter a string ')
s=''
s1=''
for i in n:
    if i not in s:
        s=s+i
    elif i not in s1:
        s1=s1+i
print('second rec :',s1[1])
print('first rec :',s1[0])
print('last rec :',s1[-1])


