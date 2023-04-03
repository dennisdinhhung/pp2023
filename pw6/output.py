import numpy as np
import zipfile
import pickle

# from domains import Information
# from domains import Student
# from domains import Course
# from input import intro

#TODO: when loading data, convert the line into an object that is manipulatible ( use split() )
#TODO: create a new function to output the data into a txt file
#TODO: create a new func to compress the data
#TODO: create a new func/option to load data from the .dat or .zip file 

def output_student_list(student_list):
    print("The student list: ")
    for student in student_list:
        print(f'{student.name} | {student.id} | {student.dob}')

def output_course_list(course_list):
    print("The course list: ")
    for course in course_list:
        print(f'{course.name} | {course.id}')

def create_marks(course_list, student_list):
    input_course_id = input('\nPlease enter the course ID: ')

    for course in course_list:
        if input_course_id != course.id:
            continue
        for student in student_list:
            student_name = student.name
            mark = input(f'\nPlease enter the mark for student {student_name}: ')
            course.add_mark(student_name, mark)

def output_marks_list(course_list):
    input_course = input('Please enter the course ID you want to see the marks of: ')
    for course in course_list:
        if course.id == input_course:
            print(course.mark_list)
            return
        
def average_gpa(course_list, student_list):
    student_mark_list = []
    input_student_id = input('Input student id to see GPA: ')
    for student in student_list:
        if student.id != input_student_id:
            continue
        for course in course_list:
            for mark_entry in course.mark_list:
                if student.name != mark_entry['name']:
                    continue
                student_mark_list.append(mark_entry['mark'])
    print(f"The average GPA of student {input_student_id} is: {np.average(student_mark_list)}")

def save_data(student_list, course_list):
    with open('data/students.pkl', 'wb') as student_file:
        pickle.dump(student_list, student_file, pickle.HIGHEST_PROTOCOL)

    with open('data/courses.pkl', 'wb') as course_file:
        pickle.dump(course_list, course_file, pickle.HIGHEST_PROTOCOL)
        
def compress_to_dat():
    with zipfile.ZipFile('data/students.dat', 'w', compression=zipfile.ZIP_DEFLATED) as zip:
        zip.write('data/students.pkl')
        zip.write('data/courses.pkl')