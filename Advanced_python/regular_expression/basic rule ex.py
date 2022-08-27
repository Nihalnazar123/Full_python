# it is used to match strings

# import re
# matcher=re.finditer('ab','ababaaabbbab')  #finditer is used to match string in a sentence
# count=0
# for i in matcher:
#     print(i.start())  #it used to find the starting of the string
#     print(i.group())   #it is used to find the which string is matched
#     count+=1
# print('match count :',count)




# basic rules example with string matching
import re
x='[abc]'
matcher=re.finditer(x,'arf ahbc @123 ABC')  #finditer is used to match string in a sentence
count=0
for i in matcher:
    print(i.start())  #it used to find the starting of the string
    print(i.group())   #it is used to find the which string is matched
    count+=1
print('match count :',count)



import re
x='[^abc]'
matcher=re.finditer(x,'arf ahbc @123 ABC')  #finditer is used to match string in a sentence
count=0
for i in matcher:
    print(i.start())  #it used to find the starting of the string
    print(i.group())   #it is used to find the which string is matched
    count+=1
print('match count :',count)


import re
x='[a-z]'
matcher=re.finditer(x,'arf ahbc @123 ABC')  #finditer is used to match string in a sentence
count=0
for i in matcher:
    print(i.start())  #it used to find the starting of the string
    print(i.group())   #it is used to find the which string is matched
    count+=1
print('match count :',count)

import re
x='[A-Z]'
matcher=re.finditer(x,'arf ahbc @123 ABC')  #finditer is used to match string in a sentence
count=0
for i in matcher:
    print(i.start())  #it used to find the starting of the string
    print(i.group())   #it is used to find the which string is matched
    count+=1
print('match count :',count)


import re
x='\d'
matcher=re.finditer(x,'arf ahbc @123 ABC')  #finditer is used to match string in a sentence
count=0
for i in matcher:
    print(i.start())  #it used to find the starting of the string
    print(i.group())   #it is used to find the which string is matched
    count+=1
print('match count :',count)