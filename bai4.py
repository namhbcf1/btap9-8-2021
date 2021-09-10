class BankAccount:
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    def Deposit(self , d ):
        self.balance = self.balance + d
    
    def Withdrawal(self , w):
        if(self.balance < w):
            print("vui long nap them tien")
        else:
            self.balance = self.balance - w
    def bankFees(self):
        self.balance = (5/100)*self.balance
        
    def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)    
        print("Account Balance : " , self.balance , " $")
        


def main():
    
    a=int(input("Enter accountNumber : "))
    b=str(input("Enter Account name : "))
    c=int(input("Enter Account balance = "))   
    e=int(input("Enter Deposit you want = "))
    w=int(input("Enter Withdrawal you want = "))
    
    newAccount = BankAccount(a, b , c)
    newAccount.Withdrawal(w)
    newAccount.Deposit(e)
    if BankAccount.Withdrawal(w) < c:
        newAccount.display()
    else:
        print("vui long nap them tien")
if __name__ == '__main__':
    main()
