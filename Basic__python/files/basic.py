# read
# write
# append


# read
# f=open('data1.txt','r')
# for i in f:
#     print(i)

# for stripping any thing.
f=open('data.txt', 'r')
for i in f:
    d=i.strip('\n')
    print(d)
