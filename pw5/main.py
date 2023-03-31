import os

from input import intro
from output import output_student_list
from output import output_course_list
from output import create_marks
from output import output_marks_list
from output import averageGpa
from domains import Student
from domains import Course

def main():
    course_list = []
    student_list = []

    while (True):
        choice = intro()

        if choice == 1:
            # create new student
            num_student = input('Input number of student(s): ')
            for i in range(int(num_student)):
                print('\n')
                input_student_id = input('Input student ID: ')
                input_student_name = input('Input student name: ')
                input_student_dob = input('Input student Date of Birth: ')
                new_student = Student(input_student_id, input_student_name, input_student_dob)
                student_list.append(new_student)
        elif choice == 2:
            # create new course
            num_course = input('Input number of course(s): ')
            for i in range(int(num_course)):
                print('\n')
                input_course_id = input('Input course ID: ')
                input_couse_name = input('Input course name: ')
                input_credits = input('Input number of credits: ')
                new_course = Course(input_course_id, input_couse_name, input_credits)
                course_list.append(new_course)
        elif choice == 3:
            # show all students
            output_student_list(student_list)
        elif choice == 4:
            # show all courses
            output_course_list(course_list)
        elif choice == 5:
            # create marks
            create_marks(course_list)
        elif choice == 6:
            # show all marks of a course
            output_marks_list(course_list)
        elif choice == 7:
            averageGpa(course_list, student_list)
        elif choice == 8:
            #import data
            print('\n')
            if not os.path.isfile("./data/students.txt"):
                print('File does not exists')
            with open('./data/students.txt', 'r+') as students_data, \
                open('./data/courses.txt', 'r+') as courses_data, \
                open('./data/marks.txt', 'r+') as marks_data:
                #TODO: strip "\n" off the data
                temp_list = [line.strip('\n') for line in students_data.readlines()]
                #TODO: process the student_list here
                for item in temp_list:
                    item_stripped = item.split(',')
                    print(item_stripped)
                    temp_student = Student(item_stripped[0], item_stripped[1], item_stripped[2])
                    student_list.append(temp_student)

                course_list = [line.strip('\n') for line in students_data.readlines()]
                mark_list = [line.strip('\n') for line in students_data.readlines()]
                # print(student_list)

        elif choice == 9:
            # save and exit
            #TODO: when output, put info into format: ex for student: "name, id, dob"
            
            return

if __name__=="__main__":
    main()