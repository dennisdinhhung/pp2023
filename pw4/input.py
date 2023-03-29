def intro():
    print('\n')
    print('What would you like to do:')
    print('(1) Create new student')
    print('(2) Create a new course')
    print('(3) See list of students')
    print('(4) See list of courses')
    print('(5) Add marks to course')
    print('(6) See marks of students in a course')
    print('(7) See average GPA of a student')
    print('(8) Exit')
    choice = int(input('Please input your choice: '))
    return choice