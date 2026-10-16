import curses
from persistence import save_data
from Domain.students import Student
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

    save_data(students)
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
    
    save_courses_txt(students)
    save_marks_txt(students)
    
    stdscr.addstr(3 + n * 3, 0, "Done! Press any key...")
    stdscr.refresh()
    stdscr.getch()