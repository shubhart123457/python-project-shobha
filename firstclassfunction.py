# First-Class Functions ki Mukhya 4 Khaasiyat:
# 1. Variables mein assign karna: Aap kisi function ko uthakar ek variable ko de sakte hain.
# 2. Arguments ke taur par pass karna: Aap ek function ko doosre function ke andar argument (input) ke roop mein bhej sakte hain.
# 3. Function se return karna: Aap ek function ke andar se doosra function return kar sakte hain.
# 4. Data Structures mein rakhna: Aap functions ko list, tuple, ya dictionary ke andar bhi store karke rakh sakte hain.


#Example 1: Assigning a function to a variable 
# None 
# def greet(): 
#  print("Hello!") 
# say_hello = greet 
# say_hello()


#Example 2: Storing functions in a list 
# None 
# def add(): 
#  print("Addition") 
# def subtract(): 
#  print("Subtraction") 
# operations = [add, subtract] 
# operations[0]() 
# operations[1]()


#Example 3: Passing a function as an argument 
 
# def greet(): 
#  print("Welcome to Python") 
# def execute_function(func): 
#  func() 
# execute_function(greet) 




# #Function ko Variable mein assign karna:

# def wish(name):
#     return f"Hello, {name}"

# # Function ko ek variable 'greet' mein assign kar diya
# greet = wish

# # Ab hum 'greet' variable ko function ki tarah call kar sakte hain
# print(greet("Amit"))  # Output: Hello, Amit


#2. Function ko doosre function mein argument ke taur par pass karna:


# def square(x):
#     return x * x

# def my_map(func, numbers):
#     result = []
#     for num in numbers:
#         result.append(func(num))  # Pass kiye gaye function ko call kar rahe hain
#     return result

# nums = [1, 2, 3, 4]
# # Yahan 'square' function ko argument ke roop mein pass kiya gaya hai
# squared_nums = my_map(square, nums)
# print(squared_nums)  # Output: [1, 4, 9, 16]



#3. Function ke andar se doosra function return karna:


# def outer_func(msg):
#     def inner_func():
#         print(f"Message is: {msg}")
#     return inner_func  # Function ke andar se doosra function return kar rahe hain

# my_closure = outer_func("Welcome to Python!")
# my_closure()  # Output: Message is: Welcome to Python!



