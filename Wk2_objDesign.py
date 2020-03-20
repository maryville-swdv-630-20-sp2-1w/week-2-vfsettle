class CheckingAccount:
        def __init__(self, fName, lName, acctNum, balance =0):
            self.fName = fName
            self.lName = lName
            self.acctNum = acctNum
            self.__balance = balance
            self.history = []
            print ("Welcome", self.fName, self.lName,", this is a deposit and withdrawal application.\n")
        
        def get_fName (self):
            return self.fName
        
        def get_lName (self):
            return self.lName
        
        def get_acctNum (self):
            return self.acctNum
        
        def get_balance (self):
            return self.balance
        
        def get_last(self):
            if len(self.history) < 1:
                return None
            else:
                print ("\n Your most recent transaction was")
                return self.history.pop()

        def viewBal (self):
            print("\n Your current balance is", self.__balance, "\n")
        
        def deposit (self, amount):
            self.__balance += amount
            self.history.append(+amount)
            print ("\n", amount , "Deposited for New Balance of", self.__balance, "\n")
            return amount
        
        def withdraw (self, amount):
            if self.__balance >= amount:
                self.__balance -= amount
                self.history.append(-amount)
                print (amount, "Withdrawn for New Balance of", self.__balance, "\n")
                return amount
            else:
                print("Unable to withdraw", amount, "from balance of", self.__balance, "\n")


def main():
    sample = CheckingAccount('Maven', 'Miller', 987654321)
    print (sample.get_fName())
    print (sample.get_lName())
    print (sample.get_acctNum())
    sample.deposit(600)
    sample.deposit(400)
    sample.withdraw(1500)
    sample.withdraw(200)
    print (sample.get_last())
    sample.deposit (550)
    sample.viewBal()
    print (sample.get_last())
        
main()