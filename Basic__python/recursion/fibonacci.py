# 0 1 1 2 3 5 8 13 21 34
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(10):
    print(fibonacci(i))

# fibonacci(0)=0
# fibonacci(1)=1
# fibonacci(2)=1
# fibonacci(3)=2
# fibonacci(4)=3
# fibonacci(5)=5
# ....




