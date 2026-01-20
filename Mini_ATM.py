import random
class account:
    def __init__(self,accNo,balance,pin):
        self.balance=balance
        self.accNo=accNo
        self.pin=pin
        self.history=[]
        self.pin_attempts=0
        self.locked=False
    
    def acc_validate(self):
        if(len(str(self.accNo))!=10):
            print("Please Enter a valid Account Number.")
            return False
        return True
        
    def mask_acc(self):
        return ('*'*(len(str(self.accNo))-4) + str(self.accNo)[-4:] )
    
    def verifyPin(self):
        if self.locked is True:
            print("Your card is locked due to too many incorrect attempts!, Try Later")
            return False
        entered=int(input('Enter PIN:'))
        if (entered==self.pin):
            self.pin_attempts=0
            return True
        else:
            self.pin_attempts+=1
            print("Invalid PIN!\n")
            if(self.pin_attempts>=3):
                self.locked=True
                print("Card locked! Too many incorrect attempts.\n")
            else:
                print(f"Attempts remaining:{3-self.pin_attempts}.\n")
            return False
    def verifyOtp(self):
        otp=random.randint(100000,999999)
        print(f"Otp sent:{otp}")
        userOtp=int(input("Enter OTP:"))
        if(userOtp==otp):
            return True
        else:
            print("Incorrect! OTP!\n")
    
    def secure_access(self):
        if not self.verifyPin():
            return False
        if not self.verifyOtp():
            return False
        return True
    
    def changePin(self):
        print("PIN Change Request")
        if not self.verifyOtp():
            return
        newPin=int(input('Set 4-digit security PIN:'))
        confirmPin=int(input('Confirm 4-digit security PIN:'))
        if(newPin==confirmPin and len(str(newPin))==4):
            self.pin=newPin
            print("PIN updated successfully.")
        else:
            print("PIN mismatched , Try again.\n")

        
    def getbalance(self):
        print(f"Current balance:${self.balance}")
    
    def debit(self,amount):
        if not self.verifyPin():
            return
        if(amount>self.balance):
            print("Transaction Failed : Insufficient Balance!\n")
            return
        self.balance-=amount
        self.history.append(f"-Debitted $:{amount}")
        print(f"${amount} debited from account number: {self.mask_acc()}")
        self.getbalance()

    def credit(self,amount):
        if not self.verifyPin():
            return
        self.balance+=amount
        self.history.append(f"+Creditted $:{amount}")
        print(f"${amount} credited from account number: {self.mask_acc()}")
        self.getbalance()

    def show_history(self):
        print('--Transaction History--\n')
        if not self.history:
            print("No Transaction Yet!")
        else:
            for h in self.history:
                print(" ",h)
        print()     

     #   -------Main Program-----

a=int(input("Enter 10-digit account number:"))
b=int(input(f"Enter current balance:$"))
p=int(input("Set 4-digit PIN:"))

acc1=account(a,b,p)
if not acc1.acc_validate():
    print("Restart The program.")
    exit()   #break can be used only within a loop

while True:
    print("---------------ATM MENU-------------\n" \
    "1.Check balance\n" \
    "2.Debit Amount\n" \
    "3.Credit Amount\n" \
    "4.Transaction History\n" \
    "5.Change PIN\n" \
    "6.Exit\n")

    ch=input("Choose Option:")
    if(ch=='1'):
        if acc1.verifyPin():
            acc1.getbalance()
    elif(ch=='2'):
        amt=int(input(f"Enter amount to debit:$"))
        acc1.debit(amt)
    elif(ch=='3'):
        amt=int(input(f"Enter amount to credit:$"))
        acc1.credit(amt)
    elif(ch=='4'):
        if acc1.verifyPin():
            acc1.show_history()
    elif(ch=='5'):
        acc1.changePin()
    elif(ch=='6'):
        print("Thank You for Banking with us!")
        break
    else:
        print("Invalid choice. TRY Again!\n")
