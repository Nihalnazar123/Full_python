# find the first repeating element
n=input('enter a string ') #apple
s=''
for i in n:   #app
    if i not in s:
        s=s+i           #s=ap
    else:
        print(i)    #p
        break

        