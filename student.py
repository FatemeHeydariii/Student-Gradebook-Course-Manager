class Student:

    def __init__(self, student_id, name, email):
        self.__student_id = student_id
        self.__name = name
        self.__email = email
        self.courses = []

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def enroll_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)

    def display_info(self):
        print("Student ID: ", self.__student_id)
        print("Name: ", self.__name)
        print("Email: ", self.__email)
        print("Course: ", self.courses)
