class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grades = {}
        self.passing_grades = 55

    def add_student(self, student):
        student_id = student.get_id()
        if student_id in self.students:
            print("Student already exists.")
        else:
            self.students[student_id] = student
            print("Student added successfully.")

    def add_course(self, course):
        if course.course_code in self.courses:
            print("Course already exists.")
        else:
            self.courses[course.course_code] = course
            print("Course added successfully.")


    def search_student(self, keyword):
        for student in self.students.values():
            if student.get_id() == keyword or student.get_name().lower() == keyword.lower():
                return student
        return None