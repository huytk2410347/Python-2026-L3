students = []
courses = []
marks = {}

def input_students():
    n = int(input("Number of students: "))
    for i in range(n):
        sid = input("Student id: ")
        name = input(" Student name: ")
        dob = input(" Date of birth: ")
        students.append({"id": sid, "name": name, "dob": dob})

def input_courses():
    n = int(input("Number of courses: "))
    for i in range(n):
        cid = input("Course id: ")
        name = input("Course name: ")
        courses.append({"id": cid, "name": name})
        marks[cid] = {}

def input_marks():
    cid = input("Select course id: ")
    for s in students:
        mark = float(input(f"Mark for {s['name']}:  "))
        marks[cid][s["id"]] = mark

def list_courses():
    for c in courses:
        print(c["id"], "-", c["name"])

def list_students():
    for s in students:
        print(s["id"], "-", s["name"], "-", s["dob"])

def show_marks(cid):
    for sid, mark in marks.get(cid, {}).items():
        name = next(s["name"] for s in students if s["id"] == sid)
        print(name, ":", mark)

def main():
    while True:
        print("\n1. Input students\n2. Input courses\n3. Input marks")
        print("4. List courses\n5. List students\n6. Show marks\n0. Exit")
        choice = input(">")
        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_courses()
        elif choice == "5":
            list_students()
        elif choice == "6":
            show_marks(input("Course id: "))
        elif choice == "0":
            break

main()