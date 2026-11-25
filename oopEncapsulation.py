# 3.1 Public, Protected, and Private Attributes
# 3.2 Private Attributes in Action

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Deposit must be positive")

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("Insufficient balance")
#         elif amount <= 0:
#             print("Withdrawal must be positive")
#         else:
#             self.__balance -= amount

#     def get_balance(self):
#         return self.__balance

# acc = BankAccount("Asha", 1000)

# acc.deposit(500)
# acc.withdraw(200)
# acc.withdraw(5000)
# print(acc.get_balance())


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance

# acc = BankAccount("Asha", 1000)
# print(acc.__balance)


# 3.3 Properties: Getters and Setters the Python Way

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @property
#     def marks(self):
#         return self._marks

#     @marks.setter
#     def marks(self, value):
#         if 0 <= value <= 100:
#             self._marks = value
#         else:
#             print("Marks must be between 0 and 100")

# s = Student("Asha", 82)
# print(s.marks)

# s.marks = 95
# print(s.marks)

# s.marks = 150
# print(s.marks)


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     @property
#     def area(self):
#         return self.width * self.height

# r = Rectangle(4, 5)
# print(r.area)

# r.width = 10
# print(r.area)



