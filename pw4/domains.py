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

class Information:
    def __init__(self):
        self.course_list = []
        self.student_list = []

    def output_student_list(self):
        print("The student list: ")
        for student in self.student_list:
            print(f'{student.name} | {student.id} | {student.dob}')

    def output_course_list(self):
        print("The course list: ")
        for course in self.course_list:
            print(f'{course.name} | {course.id}')
    
    def create_marks(self):
        input_course_id = input('\nPlease enter the course ID: ')

        for course in self.course_list:
            if input_course_id != course.id:
                continue
            for student in self.student_list:
                student_name = student.name
                mark = input(f'\nPlease enter the mark for student {student_name}: ')
                course.add_mark(student_name, mark)

    def output_marks_list(self):
        input_course = input('Please enter the course ID you want to see the marks of: ')
        for course in self.course_list:
            if course.id == input_course:
                print(course.mark_list)
                return
            
    def averageGpa(self):
        student_mark_list = []
        input_student_id = input('Input student id to see GPA: ')
        for student in self.student_list:
            if student.id != input_student_id:
                continue
            for course in self.course_list:
                for mark_entry in course.mark_list:
                    if student.name != mark_entry['name']:
                        continue
                    student_mark_list.append(mark_entry['mark'])
        print(f"The average GPA of student {input_student_id} is: {np.average(student_mark_list)}")