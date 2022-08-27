n=input('enter a string ')
v='aeiou'
b=''
for i in n:
    if i not in v:
        b=b+i
print(b)
