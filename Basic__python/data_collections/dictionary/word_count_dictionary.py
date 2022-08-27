# s='hello hi hello hi luminar'
s=input('enter some strings')
dict={}
d=s.split(' ')
for i in d:
    if i not in dict:
        dict.update({i:1})
    else:
        val=dict[i]
        val+=1
        dict.update({i:val})
print(dict)
