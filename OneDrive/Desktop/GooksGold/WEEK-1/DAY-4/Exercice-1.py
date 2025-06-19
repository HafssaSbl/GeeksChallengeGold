class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.authenticated = False
        self.balance = balance

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
        else:
            raise Exception("Authentication failed: Invalid username or password.")

    def deposit(self, money_deposit):
        if not self.authenticated:
            raise Exception("Access denied: You must be authenticated to deposit.")
        if money_deposit <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += money_deposit

    def withdraw(self, money_withdraw):
        if not self.authenticated:
            raise Exception("Access denied: You must be authenticated to withdraw.")
        if money_withdraw <= 0:
            raise Exception("Withdrawal amount must be positive.")
        self.balance -= money_withdraw

account = BankAccount("hafssa", "1234", 100)
account.authenticate("hafssa", "1234")
account.deposit(50)
print("Balance after deposit:", account.balance)

account.withdraw(30)
print("Balance after withdrawal:", account.balance)

class ATM:
    def __init__(self, account_list, try_limit):
        # Validate account_list
        if not isinstance(account_list, list) or not all(
            isinstance(acc, BankAccount) for acc in account_list
        ):
            raise Exception("account_list must be a list of BankAccount instances")

        # Validate try_limit
        if not isinstance(try_limit, int) or try_limit <= 0:
            print("Invalid try_limit. Setting to default (2).")
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0

        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- ATM Main Menu ---")
            print("1. Log in")
            print("2. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Exiting ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    def log_in(self, username, password):
        for account in self.account_list:
            try:
                account.authenticate(username, password)
                print(f"Welcome, {username}!")
                self.show_account_menu(account)
                return
            except:
                continue

        self.current_tries += 1
        print(f"Login failed. Attempt {self.current_tries}/{self.try_limit}.")

        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down ATM.")
            exit()

    def show_account_menu(self, account):
        while True:
            print("\n--- Account Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Balance")
            print("4. Exit")

            choice = input("Choose an option: ")

            try:
                if choice == "1":
                    amount = int(input("Enter amount to deposit: "))
                    account.deposit(amount)
                    print(f"Deposit successful. New balance: {account.balance}")
                elif choice == "2":
                    amount = int(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                    print(f"Withdrawal successful. New balance: {account.balance}")
                elif choice == "3":
                    print(f"Current balance: {account.balance}")
                elif choice == "4":
                    print("Logging out...")
                    account.authenticated = False
                    break
                else:
                    print("Invalid choice. Try again.")
            except Exception as e:
                print("Error:", e)

acc1 = BankAccount("hafssa", "1234", 200)
acc2 = BankAccount("yassine", "5678", 500)
atm = ATM([acc1, acc2], try_limit=3)
