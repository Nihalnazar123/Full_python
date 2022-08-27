import re
rule='[a-zA-z0-9]+[@][g][m][a][i][l][.][c][o][m]'
f=open('MAIL.TXT','r')
for i in f:
    d=i.rstrip('\n')
    matcher = re.fullmatch(rule,d)  # fullmatch is used in case of using if condition
    if matcher is not None:
        print(d)