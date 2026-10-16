import csv 
import pandas as po

students = [
{"student_id": 1, "name": "Mr Volunteers", "age": 20},
{"student_id": 2, "name": "Mr Thinh", "age": 20},
{"student_id": 3, "name": "Mr Nhat Anh", "age": 20},
]

courses = [
    {"course_id": "A1", "title": "Python", "credits": 3},
    {"course_id": "A2", "title": "Algorithms","credits": 4}, 
]

marks = [
    {"student_id": 1, "course_id": "A1", "mark": 20},
    {"student_id": 2, "course_id": "A2", "mark": 15},
    {"student_id": 3, "course_id": "A2", "mark": 12},
]

for student in students:
    print(student["name"])

with open("student.csv", "w", newline="", encoding= "utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=["student_id", "name","age"])
    writer.writeheader()
    writer.writerows(students)

def export_csv(filename, rows):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f,fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

export_csv("students.csv", students)
export_csv("courses.csv", courses)
export_csv("marks.csv", marks)

df_students = po.read_csv("student.csv")   
df_courses = po.read_csv("courses.csv")
df_marks = po.read_csv("marks.csv")

print(df_students)
print(df_courses)
print(df_marks)

def query(df, column, value):
    return df[df[column] == value]

column = input("Column: ")
value = input("Value: ")
print(query(df_students, column, value))
