from math import floor
import numpy as np

class GeneralInfo:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Course(GeneralInfo):
    def __init__(self, id, name, credits):
        super().__init__(id, name)
        self.credits = credits
        self.mark_list = []

    def add_mark(self, student_name, mark):
        mark_entry = {
            "name": student_name,
            "mark": floor(float(mark))
        }
        self.mark_list.append(mark_entry)
        
class Student(GeneralInfo):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.dob = dob
