# Main Points:
# 1. Scope: Yeh Global Scope (LEGB rule ka 'G') ke variables par kaam karta hai.
# 2. Modification: Yeh function ke andar global variable ko read karne ke sath-sath change karne ki permission deta hai.
# 3. Zaroorat: Jab aapko function ke andar kisi global variable ki value update karni ho, tab global variable_name likhna zaroori hota hai.



# counter = 0 
# def increase(): 
#  global counter 
#  counter = 10 
# increase() 
# print(counter)




# total_students = 50 
# def add_students(): 
#  global total_students 
#  total_students += 10 
# add_students() 
# print(total_students)




# # Code Example se Samajhein:
# Example 1: Bina global keyword ke (Value change nahi hogi)


# x = 50  # Global variable

# def change_value():
#     # Yahan Python ek naya local 'x' bana dega, global 'x' ko nahi badlega
#     x = 100 
#     print("Function ke andar x:", x)

# change_value()
# print("Function ke bahar x:", x)  # Output: 50 hi rahega, change nahi hua!



# Example 2:
# global keyword ke sath (Value change ho jayegi

# x = 50  # Global variable

# def change_value():
#     global x  # Python ko bata rahe hain ki hum global wale 'x' ko modify kar rahe hain
#     x = 100   
#     print("Function ke andar x:", x)

# change_value()
# print("Function ke bahar x:", x)  # Output: 100 ho gaya!