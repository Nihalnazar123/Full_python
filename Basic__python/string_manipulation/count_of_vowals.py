# method 1
# n=input('enter a string ')
# count=0
# o='aeiou'
# for i in n:
#     for j in o:
#         if i==j:
#             count+=1
# print(count)

# method 2
n=input('enter a string ')
count=0
o='aeiou'
for i in n:
    if i in o:
        count+=1
print(count)