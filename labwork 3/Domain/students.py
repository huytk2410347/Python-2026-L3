import math
import numpy as np

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