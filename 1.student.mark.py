information = {
    'student_num': 0,
    'student_list': [],
    'course_num': 0,
    'course_list': []
}

student_info = {
    'student_id': '',
    'student_name': '',
    'student_dob': '',
}

course_info = {
    'course_id': '',
    'course_name': '',
    'course_score': {
        'student_name': '',
        'score': 0,
    },
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
    information['student_num'] = input('Input number of student: ')
    student_info['student_id'] = input('Input student ID: ')
    student_info['student_name'] = input('Input student name: ')
    student_info['student_dob'] = input('Input student Date of Birth: ')
    information['student_list'].append(student_info)

def create_new_course():
    information['course_num'] = input('Input number of courses: ')
    course_info['course_id'] = input('Input course ID: ')
    course_info['course_name'] = input('Input course name: ')
    information['course_list'].append(course_info)

def create_marks():
    pass

def get_marks():
    pass

def main():
    print('')
    choice = intro()

    if (choice == 1):
        create_new_student()
        main()
    elif (choice == 2):
        main()
        create_new_course()
    elif (choice == 3):
        for student in information['student_list']:
            print(student)
        main()
    elif (choice == 4):
        for course in information['course_list']:
            print(course)
        main()
    elif (choice == 5):
        pass
    elif (choice == 6):
        pass
    elif (choice == 7):
        return

if __name__=="__main__":
    main()