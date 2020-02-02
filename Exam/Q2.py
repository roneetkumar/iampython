from random import randint


class BankAccount:
    money = 0
    type = ""

    def __init__(self):
        # self.money = money
        pass

    def setAccType(self, type):
        self.type = type

    def make_account(self):
        self.id = randint(1111, 9999)
        print(f"Your user id is {self.id}")
        self.password = input("Please enter a password for your account")

    def showbalance(self):
        print(f"balance is {self.money}")


class User:
    id = ""
    password = ""
    account = None

    def __init__(self, id, password):
        self.id = id
        self.password = password

    def deposit(self, money):
        self.account.money += money
        print(
            f"sucessfully deposit your current balance is : {self.account.money}")

    def withdraw(self, money):
        self.account.money -= money
        print(
            f"sucessfully withdrawl your current balance is : {self.account.money}")

    def remove_account(self):
        account = None
        print("account has been closed")


allUsers = []
loggedUser = None

while True:
    print("1. Create account")
    print("2. Login")
    print("Q. Quit")

    choice = input("Select Option: ")

    if choice == "1":
        id = str(randint(1111, 9999))
        print(f"Your user id is {id}")
        password = input("Please enter a password for your account: ")
        user = User(id, password)
        print("Account type")
        print("1. Savings")
        print("2. Credit")
        type = input("Select :")
        user.account = BankAccount()

        if type == '1':
            user.account.setAccType("Savings")
        elif type == '2':
            user.account.setAccType("Credit")

        allUsers.append(user)
        print("Account create sucessfully")

    elif choice == "2":
        intid = input("Enter ID : ")
        intpassword = input("Enter Password :")

        for oneUser in allUsers:
            if oneUser.id == intid and oneUser.password == intpassword:
                loggedUser = oneUser
        if loggedUser != None:
            print("\n\nLogged In")
            print("Account Number : ", loggedUser.id)
            print("Account Type: ", loggedUser.account.type)
        else:
            print("wrong id or password")

        while loggedUser != None:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance")
            print("4. Remove Account")
            print("Q. Logout")
            select = input("Select Option: ")
            if select == "1":
                amount = int(input("Enter the amount : "))
                loggedUser.deposit(amount)
            elif select == "2":
                amount = int(input("Enter the amount : "))
                loggedUser.withdraw(amount)
            elif select == "3":
                loggedUser.account.showbalance()
            elif select == "4":
                loggedUser.remove_account()
                allUsers.remove(loggedUser)
                loggedUser = None
                break
                pass
            elif select.upper() == "Q":
                break

    elif choice.upper() == "Q":
        break
