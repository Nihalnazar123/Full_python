u=int(input('enter the initial range'))
f=int(input('enter the final range'))
for i in range(u,f+1):
    for j in range(i):
        print(1,end=" ")
    print()
for s in range(f,u-1,-1):
    for a in range(s):
        print(2,end=" ")
    print()
for b in range(u,f+1):
    for c in range(b):
        print(3,end=" ")
    print()
for d in range(f,u-1,-1):
    for e in range(d):
        print(4,end=" ")
    print()