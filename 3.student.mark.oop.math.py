from math import floor
import numpy as np

class GeneralInfo:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Course(GeneralInfo):
    def __init__(self, id, name, credits, mark_list=[]):
        super().__init__(id, name)
        self.credits = credits
        self.mark_list = mark_list

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
    def __init__(self, course_list, student_list):
        self.course_list = course_list
        self.student_list = student_list

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
                    if student.name != mark_entry.student_name:
                        continue
                    student_mark_list.append(mark_entry.mark)
        print(student_mark_list)
        
def intro():
    print('\n')
    print('What would you like to do:')
    print('(1) Create new student')
    print('(2) Create a new course')
    print('(3) See list of students')
    print('(4) See list of courses')
    print('(5) Add marks to course')
    print('(6) See marks of students in a course')
    print('(7) Exit')
    choice = int(input('Please input your choice: '))
    return choice

def main():
    information = Information([], [])

    while (True):
        choice = intro()
        print(choice)

        if choice == 1:
            # create new student
            num_student = input('Input number of student(s): ')
            for i in range(int(num_student)):
                input_student_id = input('Input student ID: ')
                input_student_name = input('Input student name: ')
                input_student_dob = input('Input student Date of Birth: ')
                new_student = Student(input_student_id, input_student_name, input_student_dob)
                information.student_list.append(new_student)
        elif choice == 2:
            # create new course
            num_course = input('Input number of course(s): ')

            for i in range(int(num_course)):
                input_course_id = input('Input course ID: ')
                input_couse_name = input('Input course name: ')
                input_credits = input('Input number of credits: ')
                new_course = Course(input_course_id, input_couse_name, input_credits)
                information.course_list.append(new_course)
        elif choice == 3:
            # show all students
            information.output_student_list()
        elif choice == 4:
            # show all courses
            information.output_course_list()
        elif choice == 5:
            # create marks
            information.create_marks()
        elif choice == 6:
            # show all marks of a course
            information.output_marks_list()
        elif choice == 7:
            # exit
            return

if __name__=="__main__":
    main()