class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        if len(name) >= 2 and len(name) <= 10:
            self.name = name
        else:
            print("Invalid. Name must be between 2-10 characters.")

    def change_pin(self, pin):
        if len(str(pin)) == 4 and type(pin) == int:
            self.pin = pin
        else:
            print("Invalid. PIN must be 4 numbers.")

    def change_password(self, password):
        if len(password) >= 5:
            self.password = password
        else:
            print("Invalid. Password must be at least 5 characters.")


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    def show_balance(self):
        print(f"{self.name} has an account balance of: {self.balance:.2f}")

    def toggle_on_hold(self):
        self.on_hold = not self.on_hold

    def withdraw(self, amt):
        if self.on_hold == False:
            if type(amt) == int and amt > 0:
                if amt <= self.balance:
                    self.balance -= amt
                else:
                    print("Insufficient funds. Transaction canceled.")
            else:
                print("Invalid. Withdrawal canceled. Please enter a positive $ amount.")
        else:
            print(f"{self.name}'s account is on hold. Transaction canceled.")

    def deposit(self, amt):
        if self.on_hold == False:
            if type(amt) == int and amt > 0:
                self.balance += amt
            else:
                print("Invalid. Deposit canceled. Please enter a positive $ amount")
        else:
            print(f"{self.name}'s account is on hold. Transaction canceled.")

    def transfer_money(self, user, amt):
        if self.on_hold == False and user.on_hold == False:
            if type(amt) == int and amt > 0:
                if amt <= self.balance:
                    print(f"\nYou are transferring ${amt} to {user.name}")
                    print("Authentication required")
                    pin = int(input("Enter your PIN: "))
                    if pin == self.pin:
                        print("Transfer authorized")
                        print(f"Transferring ${amt} to {user.name}")
                        self.balance -= amt
                        user.balance += amt
                        return True
                    else:
                        print("Invalid PIN. Transaction canceled.")
                        return False
                else:
                    print("Insufficient funds. Transaction canceled.")
                    return False
            else:
                print("Invalid. Please enter a positive $ amount")
                return False
        elif self.on_hold == True and user.on_hold == True:
            print("Both accounts on hold. Transaction canceled.")
        elif self.on_hold == True:
            print(f"{self.name}'s account is on hold. Transaction canceled.")
        elif user.on_hold == True:
            print(f"{user.name}'s account is on hold. Transaction canceled.")

    def request_money(self, user, amt):
        if self.on_hold == False and user.on_hold == False:
            if type(amt) == int and amt > 0:
                if amt <= self.balance:
                    print(f"\nYou are requesting ${amt} from {user.name}")
                    print("User authentication is required...")
                    pin = int(input(f"Enter {user.name}'s PIN: "))
                    if pin == user.pin:
                        password = input("Enter your password: ")
                        if password == self.password:
                            print("Request authorized")
                            print(f"{user.name} sent ${amt}")
                            user.balance -= amt
                            self.balance += amt
                            return True
                        else:
                            print("Invalid password. Transaction canceled.")
                            return False
                    else:
                        print("Invalid PIN. Transaction canceled.")
                        return False
                else:
                    print("Insufficient funds. Transaction canceled.")
                    return False
            else:
                print("Invalid. Please enter a positive $ amount.")
                return False
        elif self.on_hold == True and user.on_hold == True:
            print("Both accounts on hold. Transaction canceled.")
        elif self.on_hold == True:
            print(f"{self.name}'s account is on hold. Transaction canceled.")
        elif user.on_hold == True:
            print(f"{user.name}'s account is on hold. Transaction canceled.")


#    """ Driver Code for Task 1 """
""" user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password) """

#    """ Driver Code for Task 2 """
""" user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)
user1.change_name("Bobby")
user1.change_pin(4321)
user1.change_password("newpassword")
print(user1.name, user1.pin, user1.password) """

#    """ Driver Code for Task 3 """
""" user1 = BankUser("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password, user1.balance) """

#    """ Driver Code for Task 4 """
""" user1 = BankUser("Bob", 1234, "password")
user1.show_balance()
user1.deposit(2000)
user1.show_balance()
user1.withdraw(1000)
user1.show_balance() """

#    """ Driver Code for Task 5 """
user1 = BankUser("Bob", 1234, "password1")
user2 = BankUser("Alice", 5678, "password2")
user2.deposit(5000)
user2.show_balance()
user1.show_balance()
if user2.transfer_money(user1, 500) == True:
    user2.show_balance()
    user1.show_balance()
    user2.request_money(user1, 250)
    user2.show_balance()
    user1.show_balance()
else:
    user2.show_balance()
    user1.show_balance()
