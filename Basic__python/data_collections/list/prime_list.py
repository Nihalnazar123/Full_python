l=[1,2,3,4,5,6,7,8,9]
prime=[]
nonprime=[]
for i in l:
    for j in range(2,i):
        if i % j == 0:
            nonprime.append(i)
            break
    else:
        prime.append(i)
print(prime)
print(nonprime)



