# f = open("dummy.txt", "r")



# with open("hello shobha", "w") as f:
#     f.write("Python\n")
#     f.write("JavaScript\n")
#     f.write("HTML\n")



# languages = ["Python\n", "JavaScript\n", "HTML\n", "CSS\n"]

# with open("dummy.txt", "w") as f:
#     f.writelines(languages)




# f = open("dummy.txt", "r")
# print(f.read())
# f.close()



# with open("dummy.txt", "r") as f:
#     print(f.tell())        # 0  (start of file)
#     print(f.read(3))       # App
#     print(f.tell())        # 3  (after 3 characters)
#     f.seek(0)              # go back to the beginning
#     print(f.readline())    # Apple




# with open("dummy.txt", "r") as f:
#     for line in f:
#         print(line.strip())



# w+ : erases the file, then you can write and read
# with open("dummy.txt", "w+") as f:
#     f.write("abc")
#     f.seek(0)             # move back to start before reading
#     print(f.read())       # abc



# a+ : writes at the end, then you can read
# with open("dummy.txt", "a+") as f:
#     f.write("def")
#     f.seek(0)
#     print(f.read())       # abcdef


# r+ : file must exist, does not erase it
# with open("dummy.txt", "r+") as f:
#     print(f.read())       # abcdef
#     f.seek(0)
#     f.write("XYZ")        # overwrites the first 3 characters
#     print(f.read())   




# with open("dummy.txt", "r") as f:
#     print(f.tell())        # 0  (start of file)
#     print(f.read(3))       # App
#     print(f.tell())        # 3  (after 3 characters)
#     f.seek(0)              # go back to the beginning
#     print(f.readline())    # Apple


# f = open("dummy.txt", "w")
# f.write("hello")
# f.close()

# f = open("dummy.txt", "r")
# print(f.read())
# f.close()

# with open("dummy.txt", "w") as f:
#     f.write("hello 2")

# with open("dummy.txt", "r") as f:
#     print(f.read())



# import os

# print(os.getcwd())




# try:
#     with open("abc.txt", "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File not found. Please check the file name.")


# import os

# print(os.path.exists("dummy.txt"))   # True or False
# os.rename("dummy.txt", "new.txt")    # rename a file
# #os.remove("new.txt")                 # delete a file



# import os

# if os.path.exists("dummy.txt"):
#     print("File found")
# else:
#     print("File not found")



# with open("photo.jpg", "rb") as source:
#     data = source.read()

# with open("photo_copy.jpg", "wb") as target:
#     target.write(data)


# with open("hindi.txt", "w", encoding="utf-8") as f:
#     f.write("नमस्ते")

# with open("hindi.txt", "r", encoding="utf-8") as f:
#     print(f.read())



# with open("dummy.txt", "w") as f:
#     f.write("Python")
#     f.write("Java")


#practice task

# Open student.txt in write mode
# with open("student.txt", "w") as f:
#     f.write("Aman Sharma\n")

# print("File created and name written successfully!")


# Open and read student.txt
# with open("student.txt", "r") as f:
#     content = f.read()

# print("File Content:")
# print(content)


# Open in append mode 'a' so previous content is preserved
# with open("student.txt", "a") as f:
#     f.write("Course: Python Masterclass\n")

# print("New content appended successfully!")



# Write multiple lines
# languages = ["Python\n", "JavaScript\n", "HTML\n", "CSS\n"]
# with open("languages.txt", "w") as f:
#     f.writelines(languages)

# # Read and print the content
# with open("languages.txt", "r") as f:
#     print(f.read())



# with open("languages.txt", "r") as f:
#     line1 = f.readline()
#     line2 = f.readline()
#     print("First line :", line1.strip())
#     print("Second line:", line2.strip())



# Safe writing using with
# with open("demo_safe.txt", "w") as f:
#     f.write("Safe file writing with context manager!")

# # Safe reading using with
# with open("demo_safe.txt", "r") as f:
#     text = f.read()
#     print("Read safely:", text)



# with open("languages.txt", "r") as f:
#     for index, line in enumerate(f, start=1):
#         print(f"{index}. {line.strip()}")


# filename = input("Enter file name: ")

# try:
#     with open(filename, "r") as f:
#         print("--- File Content ---")
#         print(f.read())
# except FileNotFoundError:
#     print(f"Sorry, the file '{filename}' was not found. Please check the name.")


# with open("student.txt", "r") as source_file:
#     data = source_file.read()

# with open("student_copy.txt", "w") as target_file:
#     target_file.write(data)

# print("File copied successfully into student_copy.txt!")