#2. Classes and Objects
# 2.1 Defining a Class and Creating Objects

# class Dog:
#     pass

# d1 = Dog()
# d2 = Dog()

# print(type(d1))
# print(d1 is d2)



# __init__ method  
# self keyword

#2.2 The __init__ Method and self



# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s1 = Student("Asha", 82)
# s2 = Student("Ravi", 70)

# print(s1.name, s1.marks)
# print(s2.name, s2.marks)


# class Student:
#     def show():
#         print("Hello")

# s = Student()
# s.show()



# 2.3 Methods

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def show(self):
#         print(self.name, "scored", self.marks)

#     def is_pass(self):
#         return self.marks >= 40

# s1 = Student("Asha", 82)
# s2 = Student("Ravi", 35)

# s1.show()
# s2.show()
# print(s1.is_pass())
# print(s2.is_pass())


# 2.4 Default Values


# class Student:
#     def __init__(self, name, marks=0, course="Python"):
#         self.name = name
#         self.marks = marks
#         self.course = course

# s1 = Student("Asha")
# s2 = Student("Ravi", 70, "Java")

# print(s1.name, s1.marks, s1.course)
# print(s2.name, s2.marks, s2.course)



#2.5 Reading, Changing, and Adding Attributes

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s1 = Student("Asha", 82)

# print(s1.marks)

# s1.marks = 90
# print(s1.marks)

# s1.city = "Pune"
# print(s1.city)

# print(hasattr(s1, "city"))
# print(hasattr(s1, "phone"))

# 2.6 Instance Attributes vs Class Attributes


# class Student:
#     school = "Green Valley School"
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Student.count += 1

# s1 = Student("Asha")
# s2 = Student("Ravi")

# print(s1.school)
# print(s2.school)
# print(Student.school)
# print(Student.count)



# 2.7 The __str__ Method

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def __str__(self):
#         return f"Student({self.name}, {self.marks})"

# s1 = Student("Asha", 82)
# print(s1)
# print(str(s1))



# 2.8 A Complete Example

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.marks = []

#     def add_mark(self, mark):
#         self.marks.append(mark)

#     def average(self):
#         if not self.marks:
#             return 0
#         return sum(self.marks) / len(self.marks)

#     def __str__(self):
#         return f"{self.name}: average {self.average():.1f}"

# s = Student("Asha")
# s.add_mark(80)
# s.add_mark(90)
# s.add_mark(70)

# print(s)
# print(len(s.marks))


# 2.9 A Common Trap: Mutable Class Attributes

# class Basket:
#     items = []

#     def add(self, item):
#         self.items.append(item)

# b1 = Basket()
# b2 = Basket()

# b1.add("apple")

# print(b2.items)


# class Basket:
#     def __init__(self):
#         self.items = []

#     def add(self, item):
#         self.items.append(item)

# b1 = Basket()
# b2 = Basket()

# b1.add("apple")

# print(b1.items)
# print(b2.items)