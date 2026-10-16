class Entity:
    """Base class: every thing we store can input() and list() itself."""
    def input(self):
        raise NotImplementedError

    def list(self):
        raise NotImplementedError


class Student(Entity):
    def __init__(self):
        self.__id = ""       # double underscore = private
        self.__name = ""
        self.__dob = ""

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def input(self):
        self.__id = input("Student id: ")
        self.__name = input("Student name: ")
        self.__dob = input("Date of birth: ")

    def list(self):
        print(f"{self.__id} - {self.__name} - {self.__dob}")


class Course(Entity):
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__marks = {}    # {student_id: mark}

    def get_id(self):
        return self.__id

    def input(self):
        self.__id = input("Course id: ")
        self.__name = input("Course name: ")

    def list(self):
        print(f"{self.__id} - {self.__name}")

    def input_marks(self, students):
        for s in students:
            self.__marks[s.get_id()] = float(input(f"Mark for {s.get_name()}: "))

    def show_marks(self, students):
        for s in students:
            print(s.get_name(), ":", self.__marks.get(s.get_id(), "no mark"))


class School:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def input_students(self):
        n = int(input("Number of students: "))
        for _ in range(n):
            s = Student()
            s.input()
            self.__students.append(s)

    def input_courses(self):
        n = int(input("Number of courses: "))
        for _ in range(n):
            c = Course()
            c.input()
            self.__courses.append(c)

    def __find_course(self):
        cid = input("Select course id: ")
        for c in self.__courses:
            if c.get_id() == cid:
                return c
        print("Course not found")
        return None

    def input_marks(self):
        c = self.__find_course()
        if c:
            c.input_marks(self.__students)

    def show_marks(self):
        c = self.__find_course()
        if c:
            c.show_marks(self.__students)

    def __list_all(self, items):
        for item in items:
            item.list()          # polymorphism: same call, different class

    def list_students(self):
        self.__list_all(self.__students)

    def list_courses(self):
        self.__list_all(self.__courses)

    def run(self):
        while True:
            print("\n1. Input students\n2. Input courses\n3. Input marks")
            print("4. List courses\n5. List students\n6. Show marks\n0. Exit")
            choice = input("> ")
            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.list_courses()
            elif choice == "5":
                self.list_students()
            elif choice == "6":
                self.show_marks()
            elif choice == "0":
                break


School().run()