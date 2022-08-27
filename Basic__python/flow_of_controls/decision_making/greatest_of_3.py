# num1
# num2
# num3
num1=int(input('enter a 1st number : '))
num2=int(input('enter a 2nd number : '))
num3=int(input('enter a 3rd number : '))
if num1==num2==num3:
    print('all 3 numbers are equal')
elif num1>=num2 and num1>=num3:
    print(num1,'is greatest')
elif num2>=num1 and num2>=num3:
    print(num2,'is greatest')
elif num3>=num1 and num3>=num2:
    print(num3,'is greatest')


















# if num1>num2 and num1>num3:
#     print('num1 is greater')
# elif num2>num1 and num2>num3:
#     print('num2 is greater')
# elif num3>num1 and num3>num2:
#     print('num3 is greater')
# elif num1 == num2 == num3:
#     print('the 3 numbers are equal')
# elif num1==num2 or num2==num3 or num3==num1:
#     if num1==num2:
#         print('1st and 2nd numbers are greater')
#     elif num2==num3:
#         print('2nd and 3rd numbers are greater')
#     elif num3 == num1:
#         print('1st and 3rd numbers are5 greater')