# function name=lambda variable:operation
add=lambda no1,no2:no1+no2
print(add(7,7))
print(add(8,6))
# ....................


# find cube using lambda
cube=lambda  no1:no1**3
print(cube(3))
print(cube(7))

# find square using lambda
square=lambda  no1:no1*no1
print(square(4))

# find even using lambda
even=lambda  no1:no1%2==0
print(even(6))
print(even(7))

string=lambda str:str[0]
print(string('hello'))

# 
rotate=lambda s:s[-2:]+s[:-2]
print(rotate('hello'))
print(rotate('world'))
