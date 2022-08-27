import re
rule='[L][U][M][p][y][\d]{4}'
f=open('registraion.txt','r')
f1=open('pythonstu.txt','w')
f2=open('datasincestu.txt','w')
for i in f:
    d=i.rstrip('\n')
    matcher = re.fullmatch(rule,d)
    if matcher is not None:
        f1.write(i)
    else:
        f2.write(i)
