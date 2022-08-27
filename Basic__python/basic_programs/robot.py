menu={'coffee':12,'black coffee':10,'latte':24}
print('Hi, Welcome to Greens coffee shop')
name=input('What is your name: ')
if name=='ben':
    print('you r not allowed here')
    exit()
print(name,'what would you like to have for todays')
print('menu:',(menu))
order=input('')
if order in menu.keys():
    quantity = int(input('how many do u need sir?: '))
    if quantity<=20:
        print('Thank you,Total price: ',menu[order]*quantity)
        print('sounds good',name, 'your',quantity, order, 'is coming up')
    else:
        print('sorry',name,'there is not enough stock available')
else:
    print('not in menu')