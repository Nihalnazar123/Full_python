import re
rule='[+][9][1][\d]{10}'
f=open('phonenumber.txt','r')
for i in f:
    d=i.rstrip('\n')
    matcher = re.fullmatch(rule, d)
    if matcher is not None:
        print(d)