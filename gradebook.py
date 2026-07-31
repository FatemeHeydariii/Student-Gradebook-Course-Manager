class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grades = {}
        self.passing_grades = 55

    def add_student(self, student):        # add student
        student_id = student.get_id()
        if student_id in self.students:
            print("Student already exists.")
        else:
            self.students[student_id] = student
            print("Student added successfully.")

    def add_course(self, course):          # add course
        if course.course_code in self.courses:
            print("Course already exists.")
        else:
            self.courses[course.course_code] = course
            print("Course added successfully.")


    def search_student(self, keyword):         # add student
        for student in self.students.values():
            if student.get_id() == keyword or student.get_name().lower() == keyword.lower():
                return student
        return None


    def enroll_student(self, student_id, course_code):      # Enroll student
            print("Student does not found.")
        if course_code not in self.courses:
            return
        student = self.students[student_id]
        course = self.courses[course_code]

student.enroll_course(course_code)
course.add_student(student_id)
        print("Student enrolled successfully.")


    def add_assessment(self, course_code, assessment):      # add assessment
        if course_code not in self.courses:
            print("Course not found.")
            return
        course = self.courses[course_code]

course.add_assessment(assessment)
        print("Assessment added successfully.")




