import curses

def show_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Student Mark Management", curses.A_BOLD)
    stdscr.addstr(1, 0, "1. Input students")
    stdscr.addstr(2, 0, "2. Input marks")
    stdscr.addstr(3, 0, "3. Show students by GPA")
    stdscr.addstr(4, 0, "4. Exit")
    curses.echo()
    stdscr.addstr(7, 0, "> ")
    stdscr.refresh()
    choice = stdscr.getstr(7, 2).decode()
    curses.noecho()
    return choice



def list_students_by_gpa(stdscr, students):
    stdscr.clear()
    ranked = sorted(students, key=lambda s: s.calculate_gpa(), reverse=True)

    stdscr.addstr(0, 0, "Students ranked by GPA", curses.A_BOLD)
    for i, s in enumerate(ranked):
        stdscr.addstr(2 + i, 0, f"{s.name} - GPA: {round(s.calculate_gpa(), 2)}")

    stdscr.addstr(3 + len(ranked), 0, "Press any key to return...")
    stdscr.refresh()
    stdscr.getch()

