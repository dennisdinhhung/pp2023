information = {
    'student_num': 0,
    'student_list': [],
    'course_num': 0,
    'course_list': []
}

def intro():
    print('What would you like to do:')
    print('(1) Create new student')
    print('(2) Create a new course')
    print('(3) See list of students')
    print('(4) See list of courses')
    print('(5) See marks of students in a course')
    print('(6) Add marks to course')
    print('(7) Exit')
    choice = int(input('Please input your choice: '))
    return choice

def create_new_student():
    student_info = {
        'student_id': '',
        'student_name': '',
        'student_dob': '',
    }

    information['student_num'] = input('Input number of student: ')
    student_info['student_id'] = input('Input student ID: ')
    student_info['student_name'] = input('Input student name: ')
    student_info['student_dob'] = input('Input student Date of Birth: ')
    information['student_list'].append(student_info)

def create_new_course():
    course_info = {
        'course_id': '',
        'course_name': '',
        'course_score': [],
    }

    information['course_num'] = input('Input number of courses: ')
    course_info['course_id'] = input('Input course ID: ')
    course_info['course_name'] = input('Input course name: ')
    information['course_list'].append(course_info)

def create_marks(information):
    course_list = information['course_list']
    student_list = information['student_list']
    input_course_id = input('\nPlease enter the course ID: ')

    for course in course_list:
        if input_course_id is not course['course_id']:
            continue
        for student in student_list:
            student_name = student['student_name']
            mark = input(f'\nPlease enter the mark for student {student_name}: ')
            course['course_score'].append({
                'student_name': student_name,
                'mark': mark
            })
    
    information['course_list'] = course_list
    return information
        
def get_marks(information):
    input_course = input('Please enter the course ID you want to see the marks of: ')
    for course in information['course_list']:
        if course['course_id'] == input_course:
            print(course['course_score'])
            return


def main(information):
    print('')
    choice = intro()

    if (choice == 1):
        create_new_student()
        main(information)
    elif (choice == 2):
        create_new_course()
        main(information)
    elif (choice == 3):
        for student in information['student_list']:
            print(student)
        main(information)
    elif (choice == 4):
        for course in information['course_list']:
            print(course)
        main(information)
    elif (choice == 5):
        get_marks(information)
        main(information)
    elif (choice == 6):
        new_information = create_marks(information)
        information = new_information
        main(information)
    elif (choice == 7):
        return

if __name__=="__main__":
    main(information)