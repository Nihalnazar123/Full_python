def prime():
    n = int(input('enter a number : '))
    m = 0
    for i in range(2, n):
        if n % i == 0:
            m = m + 1
    if m == 1:
        print('it is not a prime number')
    else:
        print('it is prime number')
prime()