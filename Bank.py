accounts = []   #This long list is for the account details
pins = []
balances = []
initialID= 123456
name = ""
handle = ""
index = 0
recip = ""
identifier = ""

f = True
class ATM:
    def __init__(self, name, initialID, balance, pocketMoney, PIN):
        self.name = name
        accounts.append(self.name)
        self.id = initialID
        initialID += 1
        self.balance = balance
        balances.append(self.balance)
        self.pocketmoney = pocketMoney
        self.pin = PIN
    def getBalance(self):     #This is used to check customer's balance, deposit, and withdraw it
        print("Rp%19d"%(self.bal))
    def getPocket(self):
        print("Rp%19d"%(self.pocketmoney))
    def withdraw(self,amount):
        self.amount = amount
        self.balance -= self.amount
        self.pocketmoney += self.amount
    def deposit(self, amount):
        self.amount2 = amount
        self.balance += self.amount2
    def debit(self, amount):
        self.amount3 = amount
        self.balance -= self.amount3
    def setPin(self, pin):    #This is used to enter PIN
        self.pin = PIN
        pins.append(self.pin)
    def transfer(self, recipient, amount):  #This is used to transfer to another custome
        global recip
        global identifier
        self.rec = recipient
        self.amount3 = amount
        identifier = ""
        if recipient in accounts:
            a = accounts.index(recipient)
            balances[a] = balances[a] + self.amount3
            handle.withdraw(self.amount3)
        else:
            print("Recipient unavailable!")

    def showAccountDetail(self):
        print("Name: ",self.name, "\nID :", self.id, "\nBalance:", self.balance)

def makeAccount(self):
    global handle
    global initialID
    handle = ATM(name, initialID, balance, pocketMoney, PIN)
    initialID += 1

while f == True:
    input("login or sign up:\n")   #To log in or sign up to a bank account
    if login.lower() == "sign up":
        name1: "First Name:\n"
        name2: "Last Name:\n"
        fullname: "name1" + "" + "name2"
        initDeposit = int(input("Enter your initial deposit:\n"))
        while True:
            pincode = int(input("Enter your 6-digit PIN:\n"))
            if len(str(pincode)) == 6:
                break
            else:
                print("You entered the wrong PIN. Please enter your correct PIN")
        makeAccount(fullname, initDeposit, 0, pincode)
        handle.showAccountDetail()   #to show the account

    elif login.lower() == "log in":
        fullname = input("Enter your full name:\n")
        if fullname in accounts:
            index = accounts.index(fullname)
            while True:
                PIN = input("Enter your 6-digit PIN:\n")
                if int(PIN)==pins[index]:
                    break
                else:
                    print("You entered the wrong PIN. Please enter your correct PIN")
        else:
            print("Account not found")
            break
        while f == true:
            dep == "1) Deposit"
            wit == "Withdraw (2"
            deb == "3) Debit"
            tra == "Transfer (4"
            qt == "5) Quit"
            print("Transactions:")
            print("-%20S %10S" % (dep, wit))
            print("-%20S %11S" % (deb, tra))
            print("-20S" % (qt))
            transaction = input("Enter your transaction type here: ")
            if transaction == "1" or transaction.lower() == "deposit":    # This is used to deposit money
                while True:
                    transaction = int(input("How much do you want to deposit?:\n"))
                    if transaction >= 0:
                        handle.deposit(transaction2)
                        print("Your balance is now: ")
                        handle.getBalance()
                        break
                    else:
                        input("Wrong amount")
            elif transaction == "2" or transaction.lower() == "Withdraw":   #This is used to withdraw money
                while True:
                    transaction = int (input("How much do you want to withdraw?:\n"))
                    if handle.balance > transaction:
                        handle.withdraw(transaction)
                        print("Your balance is now: ")
                        handle.getBalance()
                        break
                    else:
                        print("Insufficient amounts")
            elif transaction == "3" or transaction.lower() == "Debit": #to debit money
                while True:
                    transaction = int(input("How much will you be charged?\n"))
                    if handle.balance > transaction:
                        handle.debit(transaction)
                        print("Your balance is now: ")
                        handle.getbalance()
                        break
                    else:
                        print("Insufficient amounts")
            elif transaction == "4" or transaction.lower() == "Transfer":  #to transfer money
                while True:
                    for x in accounts:
                        print(x)
                    transaction = input("Enter recipient's name:\n")
                    if transaction in accounts:
                        transaction2 = int(input("Enter amount of transaction:\n"))
                        handle.transfer(transaction, transaction2)
                        print("Your balance is currently: ")
                        handle.getBalance()
                        break
                    else:
                        print("Recipient not found")
            elif transaction == "5" or transaction.lower() == "Quit": #to quit
                while True:
                    transaction = input("Are you sure? [y/n] \n")
                    if transaction.lower() == "y":
                        f == False
                        break
                    else:
                        break