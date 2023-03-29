from domains import Information
from domains import Student
from domains import Course
from input import intro

def main():
    information = Information()

    while (True):
        choice = intro()
        # print(choice)

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
            information.averageGpa()
        elif choice == 8:
            # exit
            return

if __name__=="__main__":
    main()