s1={1,2,3,4,5}
s2={3,4,5,6,7}
for i in s1:
    if i in s2:
        print(i)

# method2
print(s1.intersection(s2))