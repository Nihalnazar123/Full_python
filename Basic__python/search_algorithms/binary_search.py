# l=[1,2,3,4,5,6,7,8,0,9,22,44,55,66,87,23,99,56,64]
# e=int(input('enter a number'))
# l.sort()
# upper=l[-1]
# lower=l[0]
# while e<=upper and e>=lower:
#     middle = len(l) // 2
#     if e==l[middle]:
#         print('element found')
#         break
#     elif e<l[middle]:
#         l=l[:middle:]
#         upper=l[-1]
#         print(l)
#     elif e>l[middle]:
#         l= l[middle::]
#         lower=l[0]
#         print(l)
# else:
#     print('not found')



# method 2
l=[1,2,3,4,5,6,7,8,0,9,22,44,55,66,87,23,99,56,64]
e=int(input('enter a number'))
l.sort()
upper=len(l)-1
lower=0
flag=0
while lower<=upper:
    mid=(lower+upper)//2
    if e==l[mid]:
        flag=1
        break
    elif e>l[mid]:
        lower=mid+1
    elif e<l[mid]:
        upper=mid-1
if flag==1:
    print('present')
else:
    print('not found')





