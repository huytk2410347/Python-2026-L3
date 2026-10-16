import curses
from input import input_students, input_marks, students
from output import show_menu, list_students_by_gpa
from persistence import load_data, save_data


def main(stdscr):
    load_data(students)

    while True:
        choice = show_menu(stdscr)
        if choice == "1":
            input_students(stdscr)
        elif choice == "2":
            input_marks(stdscr)
        elif choice == "3":
            list_students_by_gpa(stdscr, students)
        elif choice == "0":
            break

    save_data(students).join()   


curses.wrapper(main)