#4.1 Single Inheritance

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"Hi, I am {self.name}, {self.age} years old.")

# class Student(Person):
#     def study(self):
#         print(self.name, "is studying")

# s = Student("Asha", 21)
# s.introduce()
# s.study()



#4.2 super() and Extending the Child

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, course):
#         super().__init__(name, age)
#         self.course = course

# s = Student("Asha", 21, "Python")
# print(s.name, s.age, s.course)



#4.3 Method Overriding

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def introduce(self):
#         print(f"Hi, I am {self.name}.")

# class Student(Person):
#     def __init__(self, name, course):
#         super().__init__(name)
#         self.course = course

#     def introduce(self):
#         super().introduce()
#         print(f"I study {self.course}.")

# p = Person("Ravi")
# s = Student("Asha", "Python")

# p.introduce()
# s.introduce()



#4.4 Checking Relationships: isinstance() and issubclass()

# class Person:
#     pass

# class Student(Person):
#     pass

# s = Student()

# print(isinstance(s, Student))
# print(isinstance(s, Person))
# print(isinstance(s, str))
# print(issubclass(Student, Person))
# print(issubclass(Person, Student))



#4.5 Multilevel Inheritance

# class Vehicle:
#     def start(self):
#         print("Vehicle started")

# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")

# class ElectricCar(Car):
#     def charge(self):
#         print("Car is charging")

# e = ElectricCar()
# e.start()
# e.drive()
# e.charge()



#4.6 Multiple Inheritance

# class Flyer:
#     def fly(self):
#         print("Flying")

# class Swimmer:
#     def swim(self):
#         print("Swimming")

# class Duck(Flyer, Swimmer):
#     pass

# d = Duck()
# d.fly()
# d.swim()



