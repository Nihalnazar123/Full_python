# swaping
num1=10
num2=20
print(num1,'before swaping num1')
print(num2,'before swaping num2')

# swaping change the content of num1 to num2 and num2 to num1
# method 1
# using temp variable
temp=num1
num1=num2
num2=temp
print('after swaping num1',num1)
print('after swaping num2',num2)


# method 2 (tuple unpacking method)
num1,num2=num2,num1
print('after swaping num1',num1)
print('after swaping num2',num2)


# method 3 (using addition and subtraction)
num1=num1+num2 #num1=30
num2=num1-num2 #num2=10
num1=num1-num2 #num1=20
print('after swaping num1',num1)
print('after swaping num2',num2)
