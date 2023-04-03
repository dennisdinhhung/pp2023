import os
from zipfile import ZipFile

from input import intro
from output import compress_to_dat, output_student_list
from output import save_data
from output import output_course_list
from output import create_marks
from output import output_marks_list
from output import average_gpa
from domains import Student
from domains import Course

def main():
    course_list = []
    student_list = []
    mark_list = []

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
            create_marks(course_list, student_list)
        elif choice == 6:
            # show all marks of a course
            output_marks_list(course_list)
        elif choice == 7:
            average_gpa(course_list, student_list)
        elif choice == 8:
            #import data
            print('\n')

            if not os.path.isfile("./data/students.dat"):
                print('(.dat) file does not exists')
            with ZipFile('./data/students.dat', 'r') as zip:
                zip.extractall()
            with open('./data/students.txt', 'r+') as students_data, \
                open('./data/courses.txt', 'r+') as courses_data, \
                open('./data/marks.txt', 'r+') as marks_data:
                temp_student_list = [line.strip('\n') for line in students_data.readlines()]
                for item in temp_student_list:
                    item_stripped = item.split(',')
                    temp_student = Student(item_stripped[0], item_stripped[1], item_stripped[2])
                    student_list.append(temp_student)
                print(student_list)

                temp_course_list = [line.strip('\n') for line in courses_data.readlines()]
                for item in temp_course_list:
                    item_stripped = item.split(',')
                    temp_course = Course(item_stripped[0], item_stripped[1], item_stripped[2])
                    course_list.append(temp_course)
                print(course_list)

                mark_list = [line.strip('\n') for line in marks_data.readlines()]
                for item in mark_list:
                    for course in course_list:
                        if item == course.id:
                            course.mark_list.append(item)
                # print(student_list)
                print('Import Successful!')

        elif choice == 9:
            # save and exit
            #TODO: when output, put info into format: ex for student: "name, id, dob"
            save_data(student_list, course_list)
            compress_to_dat()
            return

if __name__=="__main__":
    main()