u=int(input('enter a number : '))
if u%15==0:
    print('fizzbuzz')
elif u%5==0:
    print('buzz')
elif u%3==0:
    print('fizz')
else:
    print('invalid')