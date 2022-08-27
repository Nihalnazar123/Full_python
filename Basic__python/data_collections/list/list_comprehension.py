# list comprehension
# it is uesd to give code in the empty list in a single line

# l=[1,2,3,4,5,6]
# cube=[]
# for i in l:
#     cube.append(i**3)
# print(cube)


# list comprehension method
# l=[1,2,3,4,5,6]
# cube=[i**3 for  i in l]
# print(cube)

# find even using comprehension method
# l=[7,6,5,3,2,1,88,55,34]
# even=[i for i in l if i%2==0]
# print(even)


# find odd and even using comprehension method
# initial=int(input('enter a number'))
# final=int(input('enter a number '))
# even=[i for i in range(initial,final+1) if i%2==0 ]
# odd=[i for i in range(initial,final+1) if i%2!=0]
# print(even)
# print(odd)



# check the first letter of the list which begin with a then add to new list
employee=['arun','rahul','megha','bijoy','amal','anu']
new=[j for j in employee if j[0]=='a']
# for j in employee:
#     if j[0]=='a':
#         new.append(j)
print(new)






