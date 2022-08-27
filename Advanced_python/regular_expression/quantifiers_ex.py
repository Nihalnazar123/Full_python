# quantifiers
# x='a+'  a including group
# x='a*'  count including zero number of a
# x='a?' count a as each including zero no of a
# x='a{2}' 2 no of a position
# x='a{2,3}' minimum 2 a and maximum 3 a
# x='^a'  check starting with a
# x='a$' check ending with a

import re
x='a+'
matcher=re.finditer(x,'aaaa abc abbb aaabc')  #finditer is used to match string in a sentence
count=0
for i in matcher:
    print(i.start())  #it used to find the starting of the string
    print(i.group())   #it is used to find the which string is matched
    count+=1
print('match count :',count)


import re
x='a*'
matcher=re.finditer(x,'aaaa abc abbb aaabc')  #finditer is used to match string in a sentence
count=0
for i in matcher:
    print(i.start())  #it used to find the starting of the string
    print(i.group())   #it is used to find the which string is matched
    count+=1
print('match count :',count)


import re
x='a?'
matcher=re.finditer(x,'aaaa abc abbb aaabc')  #finditer is used to match string in a sentence
count=0
for i in matcher:
    print(i.start())  #it used to find the starting of the string
    print(i.group())   #it is used to find the which string is matched
    count+=1
print('match count :',count)


import re
x='a{2}'
matcher=re.finditer(x,'aaaa abc abbb aaabc')  #finditer is used to match string in a sentence
count=0
for i in matcher:
    print(i.start())  #it used to find the starting of the string
    print(i.group())   #it is used to find the which string is matched
    count+=1
print('match count :',count)

import re
x='a{2,3}'
matcher=re.finditer(x,'aaaa abc abbb aaabc')  #finditer is used to match string in a sentence
count=0
for i in matcher:
    print(i.start())  #it used to find the starting of the string
    print(i.group())   #it is used to find the which string is matched
    count+=1
print('match count :',count)


import re
x='^a'
matcher=re.finditer(x,'aaaa abc abbb aaabc')  #finditer is used to match string in a sentence
count=0
for i in matcher:
    print(i.start())  #it used to find the starting of the string
    print(i.group())   #it is used to find the which string is matched
    count+=1
print('match count :',count)


import re
x='a$'   #last index ending with a
matcher=re.finditer(x,'aaaa abc abbb aaabc')  #finditer is used to match string in a sentence
count=0
for i in matcher:
    print(i.start())  #it used to find the starting of the string
    print(i.group())   #it is used to find the which string is matched
    count+=1
print('match count :',count)


