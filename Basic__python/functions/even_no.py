def even(n):
    m=0
    if n%2==0:
        m+=1
    if m==1:
        print('it is even ')
    else:
        print('it is odd')
n=int(input('enter a number '))
even(n)
