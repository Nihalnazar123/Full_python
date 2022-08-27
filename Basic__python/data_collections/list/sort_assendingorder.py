# sort the following list
#method 1

# l=[1,6,2,4,9,8,11,3,56]
# m=[]
# for i in range(8):
#     for j in range(i+1,8):
#         if l[j]<l[i]:
#             m=l[i]
#             l[i]=l[j]
#             l[j]=m
# print(l)

# method 2
l=[1,6,2,4,9,8,11,3,56]
new=[]
while l:
    min = l[-1]
    for i in l:
        if i<min:
            min=i
    new.append(min)
    l.remove(min)
print(new)