class Course:
    def __init__(self, id, name, mark_list=[]):
        self.id = id
        self.name = name
        self.mark_list = mark_list

    def add_mark(self, mark):
        self.mark_list 

class Mark(Course):
    def __init__(self, student_name, mark):
        self.student_name = student_name
        self.mark = mark
        
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name 
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
            if input_course_id is not course.id:
                continue
            for student in self.student_list:
                student_name = student.name
                mark = input(f'\nPlease enter the mark for student {student_name}: ')
                course.add_mark(mark)

    def output_marks_list(self):
        print("The marks list: ")
        input_course = input('Please enter the course ID you want to see the marks of: ')
        for course in self.course_list:
            if course.id == input_course:
                print(course)
                return


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

        match choice:
            # create new student
            case 1:
                num_student = input('Input number of student(s): ')

                for i in range(int(num_student)):
                    input_student_id = input('Input student ID: ')
                    input_student_name = input('Input student name: ')
                    input_student_dob = input('Input student Date of Birth: ')
                    new_student = Student(input_student_id, input_student_name, input_student_dob)
                    information.student_list.append(new_student)
            # create new course
            case 2:
                num_course = input('Input number of course(s): ')

                for i in range(int(num_course)):
                    input_course_id = input('Input course ID: ')
                    input_couse_name = input('Input course name: ')
                    new_course = Course(input_course_id, input_couse_name)
                    information.course_list.append(new_course)
            # show all students
            case 3:
                information.output_student_list()
            # show all courses
            case 4:
                information.output_course_list()
            # create marks
            case 5:
                information.create_marks()
            # show all marks of a course
            case 6:
                information.output_marks_list()
            # exit
            case 7:
                return

if __name__=="__main__":
    main()