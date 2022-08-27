fixed_amnt=100000
withdrw=int(input('amount to withdraw from the account :'))
if withdrw<=100000:
    print('balance amount : ', fixed_amnt-withdrw)
else:
    print("insufficient amount")


