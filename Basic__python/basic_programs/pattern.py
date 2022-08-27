#       *
#     * *
#   * * *
# * * * *
# find the pattern

# method1
# k=8
# for i in range(5):
#     for a in range(k):
#         print(end=' ')
#     k=k-2
#     for j in range(i):
#         print('*',end=" ")
#     print()

# method2
# k=8
# for i in range(5):
#     for a in range(k):
#         print(" ",end=' ')
#     k=k-1
#     for j in range(i):
#         print('*',end=" ")
#     print()




#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# find the pattern


s=0
k=5
for i in range(5):
    for a in range(k):
        print(end=' ')
    k=k-1
    for j in range(i):
        print('*',end=" ")
    print()
for i in range(5,0,-1):
    for a in range(k):
        print(end=' ')
    k=k+1
    for j in range(i):
        print('*', end=' ')
    print()




# assignment questions

# for i in range(0,2,-1):
#     print('hello')

# x="40"
# y=int(x)+2
# print(y)

# for i in 'luminar_tech':
#     if i=='r':
#         break
