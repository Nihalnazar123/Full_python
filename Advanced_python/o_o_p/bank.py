class Bankacc:
    bankname='SBI bank '
    min=2000
    balance=2000

    def createac(self,name,acc_no):
        self.name=name
        self.acc_no=acc_no
        print(Bankacc.bankname)
        print('name: ', self.name)
        print('acc_no: ', self.acc_no)
        print('balance :', Bankacc.balance)
        print('\n')

    def depositamount(self,num1):
        self.num1=num1
        Bankacc.balance=Bankacc.balance+self.num1
        print(Bankacc.bankname)
        print('your account as been credited RS.',self.num1)
        print("balance : ",Bankacc.balance)
        print('\n')
    def withdraw(self,num2):
        self.num2=num2
        if self.min>(Bankacc.balance-self.num2):
            print(Bankacc.bankname)
            print('invalid amount or less than minimum amount')
            print('\n')
        else:
            Bankacc.balance=Bankacc.balance-self.num2
            print(Bankacc.bankname)
            print('your account as been debited RS.',self.num2)
            print('balance: ',Bankacc.balance)
            print('\n')

a1=Bankacc()
a1.createac('nihal',45782793)
a1.depositamount(10000)
a1.withdraw(1000)
a1.depositamount(5000)
a1.withdraw(15000)
a1.withdraw(4000)