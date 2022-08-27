# stack
# there is 3 types of functions in stack
# 1.push
# 2.pop
# 3.display

# push -order
# lifo-last in first out



# size=int(input('enter the size of the stack :'))
# l=[]
# while True:
#     print('1.push \n2.pop \n3.display \n4.exit')
#     option=int(input('enter the option :'))
#     if option==1:
#         if len(l)<size:
#             u = int(input('enter the number :'))
#             l.append(u)
#             print(l)
#         elif len(l)>=size:
#             print('stack overflow')
#     elif option==2:
#         if len(l)>0:
#             l.pop()
#             print(l)
#         elif len(l)==0:
#             print('stack is empty')
#     elif option==3:
#         print(l)
#     elif option==4:
#         break
#     else:
#         print('invalid number')
#
#

# method using defining function
size=int(input('enter the size '))
stack=[]
c=0
def push():
    global c
    if c>=size:
        print('stack is full')
    else:
        u=int(input('enter the number '))
        stack.append(u)
        c+=1
        print(stack)
def pop():
    global c
    if c<1:
        print('stack is empty')
    else:
        stack.pop()
        print(stack)
        c-=1
while True:
    option = int(input('1.push \n2.pop :'))
    if option==1:
        push()
    else:
        pop()

