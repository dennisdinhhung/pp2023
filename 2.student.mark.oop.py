class Mark:
    def __init__(self, student_name, mark):
        self.student_name = student_name
        self.mark = mark

    def create_mark():
        pass

class Course(Mark):
    def __init__(self, id, name, mark_list):
        self.name = name
        self.id = id
        self.mark_list = mark_list

    def create_course(self):
        super().__init__()

class Student:
    def __init__(self, name, id, dob):
        self.name = name 
        self.id = id
        self.dob = dob

    def create_student():
        pass

    def print(self):
        print(self.name)

class Information(Student, Course, Mark):
    pass

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

def main():
    new_student = Student("hung", "bi9-111", "1/1")
    new_student.print()
    new_student.name = 'stupid'
    new_student.print()

    information = Information()

    print('\n')
    choice = intro()

    match choice:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            return

if __name__=="__main__":
    main()