# important question:
# find the sum of the prime number

def prime(n,s):
    m = 0
    for i in range(n, s + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            m = m + i
    return (m)
n = int(input('enter a number : '))
s = int(input('enter a number : '))
print(prime(n,s))


