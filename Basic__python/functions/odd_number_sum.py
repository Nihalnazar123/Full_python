def odd(n,s):
    m = 0
    for i in range(n, s + 1):
        if i % 2 != 0:
            m = m + i
    return (m)
n = int(input('enter a number '))
s = int(input('enter a number '))
print(odd(n,s))