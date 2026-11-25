# import csv     #csv file ko read karne ke liye use kiya hai
# from pathlib import Path    #file ka address pata karne ke liye

# csv_file_path = Path(r"C:\Users\DeLL\OneDrive\Desktop\skilledu_sample_student_registrations_200.csv")

# grouped_students = {}   #khali dict course ke name aur student ki row banane ke liye

# if not csv_file_path.exists():    #check karne ke liye ki location par file hai ya nahi
#     print("CSV file nahi mili! Kripya path check karein:")
#     print(csv_file_path)
# else:
#     with open(csv_file_path, mode="r", encoding="utf-8-sig") as file:   #file ko read mode me open karne ke liye
#         reader = csv.DictReader(file)   #file ki har line ko dict me convert karne ke liye

#         for row in reader:      #file ki ek ek student ki row par loop chalne ke liye
#             course = row["Course"].strip()     #course ka name pata karta hai aur strip space hatane ke liye

#             if course not in grouped_students:    #curse pahli bar milta hai to ek new list bana deta hai
#                 grouped_students[course] = [row]
#             else:                  #student ko ad kar deta hai
#                 grouped_students[course].append(row)

#     # 1. Course-wise student count karne ke liye
#     print("=== Course-wise Student Count ===")
#     total_students = 0

#     for course, students in grouped_students.items():    #loop chalane ke liye
#         count = len(students)    #count ke liye
#         total_students += count      #har course ki ginti ko total student me jodne ke liye
#         print(f"- {course}: {count} students")                  

#     print(f"\nTotal Students: {total_students}\n")

#     # 2. Har course ke students ki details print karne ke liye
#     for course, students in grouped_students.items():     
#         print("=" * 75)        #divider line bana deta hai taki sabhi course ke hisab se alag dikhe
#         print(f"Course: {course} | Total Students: {len(students)}")
#         print("=" * 75)
#         for s in students:
#             print(f"{s['Student_ID']} | {s['Student_Name']} | {s['Gender']} | "f"{s['City']}, {s['State']} | Reg: {s['Registration_Date']} | {s['Learning_Mode']}")
        





import csv

course_count = {}

with open(r"C:\Users\DeLL\OneDrive\Desktop\skilledu_sample_student_registrations_200.csv") as file:
    data = csv.DictReader(file)

    for row in data:
        course = row["Course"]

        if course in course_count:
            course_count[course] += 1
        else:
            course_count[course] = 1

for course, count in course_count.items():
    print(course, ":", count)