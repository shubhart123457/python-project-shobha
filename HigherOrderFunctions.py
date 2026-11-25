#Example 1: Custom higher-order function 

# def calculate(a, b, operation): 
#  return operation(a, b) 
# def add(x, y): 
#  return x + y 
# def multiply(x, y): 
#  return x * y 
# print(calculate(10, 5, add)) 
# print(calculate(10, 5, multiply))



# Example 2: Built-in map() 
# map() is a built-in higher-order function. 
# It applies a function to every element of an iterable. 

# numbers = [1, 2, 3, 4] 
# def square(n): 
#  return n ** 2 
# result = map(square, numbers) 
# print(list(result))




# Example 3: Built-in filter() 
# filter() selects elements from an iterable based on a condition. 

# numbers = [1, 2, 3, 4, 5, 6] 
# def is_even(n): 
#  return n % 2 == 0 
# result = filter(is_even, numbers) 
# print(list(result))




#Example 4: Built-in sorted() with a function 

# students = [{"name": "Amit", "marks": 80}, {"name": "Rahul", "marks": 70}, {"name": "Riya", "marks": 95}]
# result = sorted(students, key=lambda student: student["marks"])
# print(result)
 



