import math
import numpy as np
import curses


class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob
        self.courses = {}

    def add_mark(self, course_id, credit, mark):
        self.courses[course_id] = {
            "credit": credit,
            "mark": math.floor(mark * 10) / 10
        }

    def calculate_gpa(self):
        if not self.courses:
            return 0
        credits = np.array([c["credit"] for c in self.courses.values()])
        marks = np.array([c["mark"] for c in self.courses.values()])
        return np.sum(credits * marks) / np.sum(credits)


students = []


def ask(stdscr, row, question):
    curses.echo()
    stdscr.addstr(row, 0, question)
    stdscr.refresh()
    answer = stdscr.getstr(row, len(question) + 1).decode()
    curses.noecho()
    return answer


def input_students(stdscr):
    stdscr.clear()
    n = int(ask(stdscr, 0, "Number of students: "))

    for i in range(n):
        base = 2 + i * 3
        sid = ask(stdscr, base, "Student id: ")
        name = ask(stdscr, base + 1, "Name: ")
        dob = ask(stdscr, base + 2, "Dob: ")
        students.append(Student(sid, name, dob))

    stdscr.addstr(2 + n * 3, 0, "Done! Press any key...")
    stdscr.refresh()
    stdscr.getch()


def input_marks(stdscr):
    stdscr.clear()
    sid = ask(stdscr, 0, "Student id: ")
    student = next((s for s in students if s.id == sid), None)

    if student is None:
        stdscr.addstr(2, 0, "Student not found!")
        stdscr.refresh()
        stdscr.getch()
        return

    n = int(ask(stdscr, 1, "Number of courses: "))

    for i in range(n):
        base = 3 + i * 3
        cid = ask(stdscr, base, "Course id: ")
        credit = float(ask(stdscr, base + 1, "Credit: "))
        mark = float(ask(stdscr, base + 2, "Mark: "))
        student.add_mark(cid, credit, mark)

    stdscr.addstr(3 + n * 3, 0, "Done! Press any key...")
    stdscr.refresh()
    stdscr.getch()


def list_students_by_gpa(stdscr):
    stdscr.clear()
    ranked = sorted(students, key=lambda s: s.calculate_gpa(), reverse=True)

    stdscr.addstr(0, 0, "Students ranked by GPA", curses.A_BOLD)
    for i, s in enumerate(ranked):
        stdscr.addstr(2 + i, 0, f"{s.name} - GPA: {round(s.calculate_gpa(), 2)}")

    stdscr.addstr(3 + len(ranked), 0, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()


def main(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Student Mark Management", curses.A_BOLD)
        stdscr.addstr(2, 0, "1. Input students")
        stdscr.addstr(3, 0, "2. Input marks")
        stdscr.addstr(4, 0, "3. Show students by GPA")
        stdscr.addstr(5, 0, "0. Exit")
        choice = ask(stdscr, 7, "> ")

        if choice == "1":
            input_students(stdscr)
        elif choice == "2":
            input_marks(stdscr)
        elif choice == "3":
            list_students_by_gpa(stdscr)
        elif choice == "0":
            break


curses.wrapper(main)