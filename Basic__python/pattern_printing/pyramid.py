# find
#     *
#    * *
#   * * *
#  * * * *

# s=7
# for i in range (5):
#     for a in range(s):
#         print(end=' ')
#     s=s-1
#     for j in range(i):
#          print('*',end=' ')
#     print()

# find
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# for i in range(5):
#     for j in range(5):
#         print('*',end=' ')
#     print()





# find
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
s=0
for i in range (5,0,-1):
    for a in range(s):
        print(end=' ')
    s=s+1
    for j in range(i):
         print('*',end=' ')
    print()

#find
# * * * * *
#  * * * * *
#   * * * * *
#    * * * * *
#     * * * * *
s=0
for i in range(5):
    for a in range(s):
        print(end=' ')
    s=s+1
    for j in range(5):
        print('*',end=' ')

    print()