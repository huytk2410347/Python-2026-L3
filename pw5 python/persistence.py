import os
import zipfile
from Domain.students import Student

DATA_FILE = "students.dat"


def save_students_txt(students):
    with open("students.txt", "w") as f:
        for s in students:
            f.write(f"{s.id},{s.name},{s.dob}\n")


def save_courses_txt(students):
    courses = {}
    for s in students:
        for cid, info in s.courses.items():
            courses[cid] = info["credit"]

    with open("courses.txt", "w") as f:
        for cid, credit in courses.items():
            f.write(f"{cid},{credit}\n")


def save_marks_txt(students):
    with open("marks.txt", "w") as f:
        for s in students:
            for cid, info in s.courses.items():
                f.write(f"{s.id},{cid},{info['mark']}\n")


def compress_data():
    with zipfile.ZipFile(DATA_FILE, "w") as zf:
        zf.write("students.txt")
        zf.write("courses.txt")
        zf.write("marks.txt")


def load_data(students):
    if not os.path.exists(DATA_FILE):
        return  

    with zipfile.ZipFile(DATA_FILE, "r") as zf:
        zf.extractall()

    with open("students.txt") as f:
        for line in f:
            sid, name, dob = line.strip().split(",")
            students.append(Student(sid, name, dob))

    credits = {}
    with open("courses.txt") as f:
        for line in f:
            cid, credit = line.strip().split(",")
            credits[cid] = float(credit)

    with open("marks.txt") as f:
        for line in f:
            sid, cid, mark = line.strip().split(",")
            student = next((s for s in students if s.id == sid), None)
            if student:
                student.courses[cid] = {"credit": credits[cid], "mark": float(mark)}