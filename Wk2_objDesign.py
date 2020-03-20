class CheckingAccount:
        def __init__(self):
            self.__balance = 0
            print ("This is a deposit and withdrawal application. \n Your starting balance is", self.__balance)
        
        def viewBal (self):
            print("\n Your current balance is", self.__balance)
        
        def deposit (self):
            amount = float(input("Enter Deposit Amount: "))
            self.__balance += amount
            print ("\n", amount , "Deposited for New Balance of", self.__balance)
            
        def withdraw (self):
            amount = float(input("Enter Withdrawal Amount: "))
            if self.__balance >= amount:
                self.__balance -= amount
                print (amount, "Withdrawn for New Balance of", self.__balance)
            else:
                print ("Unable to withdraw", amount, "from balance of", self.__balance)


def main():
    sample = CheckingAccount()
    sample.deposit()
    sample.deposit()
    sample.withdraw()
    sample.viewBal()
    sample.withdraw()
        
main()