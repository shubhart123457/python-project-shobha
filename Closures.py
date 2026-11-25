#Example 1: Nested functions 
 
# def outer(): 
#    message = "Hello from outer function" 
#    def inner(): 
#     print(message) 
#    inner() 
# outer() 



#Example 2: Returning an inner function 

# def outer(): 
#   message = "Hello Python" 
#   def inner(): 
#     print(message) 
#   return inner 
# my_function = outer() 
# my_function()




#Example 3: Closure with parameters 

# def multiplier(factor): 
#   def multiply(number): 
#    return number * factor 
#   return multiply 
# double = multiplier(2) 
# triple = multiplier(3) 
# print(double(10)) 
# print(triple(10))




#Closure with nonlocal

# def create_counter(): 
#   count = 0 
#   def counter(): 
#    nonlocal count 
#    count += 1 
#    return count 
#   return counter 
# counter = create_counter() 
# print(counter())  # 1 
# print(counter())  # 2 
# print(counter())  # 3




