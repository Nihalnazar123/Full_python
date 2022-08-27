# selection option
# 1.add
# 2.sub
# 3.mul
# 4.div
# 5.stop
# num1
# num2
# while true



def add():
    a = num1 + num2
    print(a)


def sub():
    s = num1 - num2
    print(s)


def mul():
    m = num1 * num2
    print(m)


def div():
    d = num1 / num2
    print(d)


while True:
    print('1.add'
          '\n2.sub'
          '\n3.mul'
          '\n4.div'
          '\n5.stop')
    u = int(input('enter the number '))
    if u==1:
        num1 = int(input('enter the number '))
        num2 = int(input('enter the number '))
        add()
    elif u==2:
        num1 = int(input('enter the number '))
        num2 = int(input('enter the number '))
        sub()
    elif u==3:
        num1 = int(input('enter the number '))
        num2 = int(input('enter the number '))
        mul()
    elif u==4:
        num1 = int(input('enter the number '))
        num2 = int(input('enter the number '))
        div()
    elif u==5:
        break
    else:
        print('invalid choice')


