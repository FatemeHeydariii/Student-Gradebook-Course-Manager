class Gradebook:

    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = 55

    # ---------------- Add Student ----------------

    def add_student(self, student):
        student_id = student.get_id()

        if student_id in self.students:
            print("Student already exists.")
        else:
            self.students[student_id] = student
            print("Student added successfully.")

    # ---------------- Add Course ----------------

    def add_course(self, course):

        if course.course_code in self.courses:
            print("Course already exists.")
        else:
            self.courses[course.course_code] = course
            print("Course added successfully.")

    # ---------------- Search Student ----------------

    def search_student(self, keyword):

        for student in self.students.values():

            if student.get_id() == keyword or student.get_name().lower() == keyword.lower():
                return student

        return None

# ---------------- Enroll Student ----------------

    def enroll_student(self, student_id, course_code):

        if student_id not in self.students:
            print("Student not found.")
            return

        if course_code not in self.courses:
            print("Course not found.")
            return

        student = self.students[student_id]
        course = self.courses[course_code]

        student.enroll_course(course_code)
        course.add_student(student_id)

        print("Student enrolled successfully.")

    # ---------------- Add Assessment ----------------

    def add_assessment(self, course_code, assessment):

        if course_code not in self.courses:
            print("Course not found.")
            return

        course = self.courses[course_code]
        course.add_assessment(assessment)

        print("Assessment added successfully.")

    # ---------------- Record Grade ----------------

    def record_grade(self, student_id, course_code, assessment_title, score):

        if student_id not in self.students:
            print("Student not found.")
            return

        if course_code not in self.courses:
            print("Course not found.")
            return

        course = self.courses[course_code]

        assessment = course.find_assessment(assessment_title)

        if assessment is None:
            print("Assessment not found.")
            return

        if score < 0 or score > assessment.max_score:
            print("Invalid score.")
            return

        if student_id not in self.grades:
            self.grades[student_id] = {}

        if course_code not in self.grades[student_id]:
            self.grades[student_id][course_code] = {}

        self.grades[student_id][course_code][assessment_title] = score

        print("Grade recorded successfully.")


# ---------------- Calculate Average ----------------

    def calculate_average(self, student_id, course_code):

        if student_id not in self.grades:
            return 0

        if course_code not in self.grades[student_id]:
            return 0

        course = self.courses[course_code]
        grades = self.grades[student_id][course_code]

        total = 0
        count = 0

        for assessment in course.assessments:

            if assessment.title in grades:

                score = grades[assessment.title]
                percent = assessment.calculate_percentage(score)

                total += percent
                count += 1

        if count == 0:
            return 0

        return total / count

    # ---------------- Pass / Fail ----------------

    def get_result(self, average):

        if average >= self.passing_grade:
            return "Passed"
        else:
            return "Failed"

    # ---------------- Student Report ----------------

    def show_report(self, student_id):

        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]

        print("\n===== Student Report =====")
        print("Student ID:", student.get_id())
        print("Name:", student.get_name())
        print("Email:", student.get_email())

        for course_code in student.courses:

            course = self.courses[course_code]

            print("\nCourse:", course.course_code, "-", course.course_name)

            if student_id in self.grades and course_code in self.grades[student_id]:

                for assessment in course.assessments:

                    if assessment.title in self.grades[student_id][course_code]:

                        score = self.grades[student_id][course_code][assessment.title]
                        percent = assessment.calculate_percentage(score)

                        print(assessment.title, ":", score, "/", assessment.max_score, "=", round(percent, 2), "%")

                average = self.calculate_average(student_id, course_code)

                print("Average:", round(average, 2))
                print("Result:", self.get_result(average))
                print("Letter Grade:", self.get_letter_grade(average))

    # ---------------- Update Student ----------------

    def update_student(self, student_id, new_email):

        if student_id not in self.students:
            print("Student not found.")
            return

        self.students[student_id].set_email(new_email)

        print("Email updated successfully.")

    # ---------------- Delete Student ----------------

    def delete_student(self, student_id):

        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]

        for course_code in student.courses:

            if course_code in self.courses:

                course = self.courses[course_code]

                if student_id in course.students:
                    course.students.remove(student_id)

        if student_id in self.grades:
            del self.grades[student_id]

        del self.students[student_id]

        print("Student deleted successfully.")


# ---------------- Letter Grade ----------------

    def get_letter_grade(self, average):

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"


# ---------------- Top Student ----------------

    def top_student(self):

        highest = -1
        top_name = ""

        for student_id in self.students:

            total = 0
            count = 0

            if student_id in self.grades:

                for course_code in self.grades[student_id]:

                    average = self.calculate_average(student_id, course_code)

                    total += average
                    count += 1

            if count > 0:

                final_average = total / count

                if final_average > highest:
                    highest = final_average
                    top_name = self.students[student_id].get_name()

        if highest == -1:
            print("No grades found.")
        else:
            print("Top Student:", top_name)
            print("Average:", round(highest,2))


# ---------------- Course Statistics ----------------

    def course_statistics(self):

        print("\n===== Course Statistics =====")

        for course in self.courses.values():

            print("\nCourse:", course.course_name)
            print("Students:", len(course.students))
            print("Assessments:", len(course.assessments))