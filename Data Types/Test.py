# class Atm:

#     def __init__(self):
#         self.balance = 0
#         self.pin = ""

#         self.menu()

#     def menu(self):
#         user_input = "Enter Your option"

#         if user_input == 1:
#             self.create_pin()
#         elif user_input == 2:
#             self.withdraw()
#         if user_input == 3:
#             self.deposit()
#         elif user_input == 4:
#             self.balance()
#         else:
#             print("Bye")

#     def create_pin(self):
#         self.pin = input("Enter your pin")
#         print(f"Print Set Successfully {self.pin}")
#     def withdraw(self):
#         if self.balance:
#             withdraw_amount = int(input("Enter the amount you want to withdraw: "))
#             self.balance = self.balance - withdraw_amount
#         print(f"Your remaining Balance is {self.balance}")

#     def deposit(self):
#         Amount = int(input("Enter the amount you want to deposit"))
#         self.balance = self.balance + Amount
#         print(f"Your Amount: {self.balance}")

#     def balance(self):
#         print(self.balance)

class Atm:
    counter = 0

    def __init__(self):
        self.sno = Atm.counter
        Atm.counter +=1

classatm = Atm()
class2atm = Atm()
print(classatm.sno)
print(class2atm.sno)