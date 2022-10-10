print("hello")

class Atm:
    def __init__(self): # it is a constructor in which when we made class object the inside constrrcutor automatically executes
        self.pin = ''
        self.balance = 0
        print(id(self))
        self.menu()

    def menu(self):
        user_input = input("""
            hello, how would you like to proceed
            1. enter 1 to create pin 
            2. enter 2 to deposit
            3. enter 3 to withdraw
            4. enter 4 to check balance
            5. enter 5 to check exit
        """)

        if user_input =="1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input =="3":
            self.withdraw()
        elif user_input=="4":
            self.c_balance()
        else: 
            print("bye")
    def create_pin (self):
        self.pin = input("enter your pin")
        print("pin set succesfully")
    
    def deposit(self):
        temp = input("enter your pin")
        if temp ==self.pin:
            amount = int(input("enter the amount "))
            self.balance = self.balance + amount
            print("deposit succesfully")
        else:
            print("invalid pin")
    def withdraw(self):
        temp = input("enter your pin")
        if temp ==self.pin:
            amount = int(input("enter the amount "))
            if amount <=self.balance:   
                self.balance = self.balance - amount
                print("Withdraw succesfully")
            else:
                print("Insufficient funds")
        else:
            print("invalid pin")

    def c_balance(self):
        temp = input("enter your pin")
        if temp ==self.pin:
            print(self.balance)
        else:
            print("invalid pin")


sel = Atm()
hdfc = Atm()
# sel.deposit()
# sel.c_balance()
print(id(sel))
print(id(hdfc))
