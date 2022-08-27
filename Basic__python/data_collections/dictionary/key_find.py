# in build method to find keys and values

person={'name':'anu','age':23,'place':'kochi'}
print(person.keys())
print(person.values())



# find the user input key
d={1:2,2:3,3:4,4:5}
u=int(input('enter the key '))
if u in d.keys():
    print('present')
else:
    print('not present')