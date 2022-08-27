n = int(input('enter a number : '))
s=int(input('enter a number : '))
for i in range(n,s+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,'it is prime number')