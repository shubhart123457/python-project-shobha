# Mukhya Bindu (Key Points):
# Scope: Yeh enclosing function scope ko refer karta hai (LEGB rule ka 'E').  
# Nested Functions Zaroori Hain: Iske liye nested functions (enclosing function binding) ka hona anivarya hai, kyunki yeh single function ya global level par kaam nahi karta.  
# Global Scope par Laagu nahi: nonlocal keyword kabhi bhi kisi aise variable ko refer nahi kar sakta jo sirf global scope mein exist karta ho.



# def outer(): 
#  count = 0 
#  def inner(): 
#   nonlocal count 
#   count = 10 
#  inner() 
#  print(count) 
# outer() 






# def outer_function():
#     message = "Hello"  # Enclosing scope ka variable
    
#     def inner_function():
#         #nonlocal message  # Batata hai ki hum outer_function ke 'message' ko modify kar rahe hain
#         message = "Hi from Inner"
#         print("Inner function mein:", message)
        
#     inner_function()
#     print("Outer function mein (change hone ke baad):", message)

# outer_function()