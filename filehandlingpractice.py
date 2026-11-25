# institute_name = "Vikram University"
# def display_student():
#     student_name = "Shobha"
#     course = "Fine Arts"
    
#     print("Institute Name:", institute_name)
#     print("Student Name:", student_name)
#     print("Course:", course)

# display_student()
# print("student_name")



# Requirement 1: Global variable create karna
# balance = 5000

# # Requirement 2 & 3: deposit(amount) function aur global keyword ka use
# def deposit(amount):
#     global balance  # Global variable ko access aur modify karne ki permission deta hai
#     balance += amount
#     print(f"Successfully Deposited: ₹{amount}")
#     print(f"Updated Balance: ₹{balance}\n")

# # Requirement 4 & 5 & 6: withdraw(amount) function, insufficient balance check aur display
# def withdraw(amount):
#     global balance
#     if amount > balance:
#         print(f"Withdrawal Failed! Insufficient balance for ₹{amount}.")
#         print(f"Available Balance: ₹{balance}\n")
#     else:
#         balance -= amount
#         print(f"Successfully Withdrawn: ₹{amount}")
#         print(f"Updated Balance: ₹{balance}\n")

# # --- Program Testing / Execution ---
# print(f"--- Initial Bank Account Status ---")
# print(f"Starting Balance: ₹{balance}\n")

# # 1. Deposit test
# deposit(2000)

# # 2. Successful withdrawal test
# withdraw(1500)

# # 3. Insufficient balance withdrawal test (Fail case)
# withdraw(8000)





# def login_system():
#     attempts = 0  # Enclosing scope variable
    
#     def login():
#         nonlocal attempts
#         attempts += 1
        
#         # Dictionary ka use karke if-else ko bypass kiya gaya hai
#         # Key `True` tab chalegi jab attempts < 3 honge, aur `False` tab jab attempts >= 3 honge.
#         messages = {True: f"Login attempt #{attempts} failed. Please try again.\n",False: f"Login attempt #{attempts} failed. Alert: Account temporarily locked due to 3 failed attempts!\n"}
        
#         # attempts < 3 ek boolean expression hai (True ya False) jo dictionary key ban jati hai
#         print(messages[attempts < 3])
#         return attempts
        
#     return login

# # --- Program Testing / Execution ---
# track_attempts = login_system()

# track_attempts()  # 1st call (attempts < 3 is True)
# track_attempts()  # 2nd call (attempts < 3 is True)
# track_attempts()  # 3rd call (attempts < 3 becomes False)





# Chaaron functions define karna
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error: Division by zero is not allowed!"
#     return a / b

# # Requirement 1 & 2: Functions ko dictionary mein store karna (operation names as keys)
# operations = {"add": add,"subtract": subtract,"multiply": multiply,"divide": divide}

# # Calculator function jo operations dictionary ka use karega
# def calculate(op_name, num1, num2):
#     # Requirement 4: Dictionary se corresponding function retrieve karna
#     selected_function = operations.get(op_name)
    
#     if selected_function:
#         # Requirement 5: Function ko do numbers ke saath execute karna
#         result = selected_function(num1, num2)
#         return result
#     else:
#         return "Invalid Operation!"

# # --- Program Testing / Execution ---
# print("--- Mathematical Operations Manager ---")

# # Requirement 3: Operations ko call karke test karna
# print("Addition (10 + 5)     :", calculate("add", 10, 5))
# print("Subtraction (10 - 5)  :", calculate("subtract", 10, 5))
# print("Multiplication (10*5):", calculate("multiply", 10, 5))
# print("Division (10 / 5)     :", calculate("divide", 10, 5))




# Given data
# marks = [45, 78, 90, 32, 65, 88, 25, 95]

# # Requirement 1: Square calculate karne ke liye function
# def calculate_square(n):
#     return n ** 2

# # Requirement 2: map() ka use karke square apply karna
# squared_marks = list(map(calculate_square, marks))

# # Requirement 3: filter() ka use karke 60 ya usse zyada marks select karna
# passed_marks = list(filter(lambda x: x >= 60, marks))

# # Requirement 4: sorted() ka use karke marks ko descending order (bade se chote) mein arrange karna
# descending_marks = sorted(marks, reverse=True)

# # Requirement 5: Apna khud ka Higher-Order Function jo function aur list accept kare
# def apply_operation(func, data):
#     return list(map(func, data))

# # Custom function test karne ke liye (jaise marks ko double karna)
# def double_marks(n):
#     return n * 2

# custom_result = apply_operation(double_marks, marks)

# # --- Program Outputs / Execution ---
# print("Original Marks:", marks)
# print("1 & 2. Squared Marks (using map):", squared_marks)
# print("3. Passed Marks >= 60 (using filter):", passed_marks)
# print("4. Descending Order (using sorted):", descending_marks)
# print("5. Custom Higher-Order Function Result (Doubled):", custom_result)



# Requirement 1 & 2: Outer function jo discount percentage accept karega
# def create_discount(discount_percent):
    
#     # Requirement 3: Inner function jo product price accept karega
#     def apply_discount(price):
#         # Requirement 4: Discounted price calculate karke return karna
#         discount_amount = (price * discount_percent) / 100
#         final_price = price - discount_amount
#         return final_price
        
#     # Requirement 5: Inner function ko return karna (Closure banata hai)
#     return apply_discount

# # --- Program Testing & Execution (Requirement 6 & Expected Usage) ---

# # Alag-alag discount ke liye calculators create karna
# discount_10 = create_discount(10)
# discount_20 = create_discount(20)
# discount_30 = create_discount(30)

# # Expected usage ke mutabik print karna
# print("10% Discount on ₹1000:", discount_10(1000))
# print("20% Discount on ₹1000:", discount_20(1000))
# print("30% Discount on ₹1000:", discount_30(1000))






# Given data
# data = [12, 45, 67, 89, 23, 90, 34, 76, 55, 100]

# # Requirement 1: Global variable to track the number of processed records
# processed_records_count = 0

# # Requirement 2: Function to filter records >= 40
# def filter_greater_than_40(value):
#     return value >= 40

# # Requirement 3: Function to normalize values by dividing by 100
# def normalize_by_100(value):
#     return value / 100

# # Requirement 5: Closure that remembers a configurable normalization factor (Bonus/Advanced Requirement)
# def configure_normalizer(factor):
#     def custom_normalize(value):
#         return value / factor
#     return custom_normalize

# # Requirement 6: Nested function with nonlocal to maintain a count of processed records
# def create_pipeline_tracker():
#     internal_count = 0  # Enclosing scope variable
    
#     def process_and_count(dataset, filter_func, normalizer_func):
#         nonlocal internal_count
#         global processed_records_count
        
#         # Requirement 4: Using higher-order functions (filter and map)
#         filtered_data = list(filter(filter_func, dataset))
#         normalized_data = list(map(normalizer_func, filtered_data))
        
#         # Count update karna
#         internal_count = len(normalized_data)
#         processed_records_count = internal_count
        
#         return normalized_data
        
#     return process_and_count

# # --- Program Execution & Testing ---

# # Pipeline instance create karna
# run_pipeline = create_pipeline_tracker()

# # Standard Normalizer (divide by 100) ya Configurable Closure normalizer use karna
# standard_normalizer = configure_normalizer(100)

# # Pipeline ko run karna
# final_dataset = run_pipeline(data, filter_greater_than_40, standard_normalizer)

# # Requirement 7: Display the final processed dataset and metrics
# print("--- ML Data Preprocessing Pipeline ---")
# print("Original Dataset             :", data)
# print("Final Processed Dataset      :", final_dataset)
# print("Processed Records Count (Global):", processed_records_count)