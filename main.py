from student import Student
from course import Course
from assessment import Quiz, Exam, Project
from gradebook import Gradebook

gradebook = Gradebook()

while True:

    print("\n========== Student Gradebook Manager ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Course")
    print("4. Enroll Student")
    print("5. Add Assessment")
    print("6. Record Grade")
    print("7. View Student Report")
    print("8. Search Student")
    print("9. Update Student Email")
    print("10. Delete Student")
    print("11. Dashboard")
    print("12. Top Student")
    print("13. Course Statistics")
    print("0. Exit")

    choice = input("Choose an option: ")

    # Add Student
    if choice == "1":

        student_id = input("Student ID: ")
        name = input("Name: ")
        email = input("Email: ")

        student = Student(student_id, name, email)
        gradebook.add_student(student)

    # View Students
    elif choice == "2":

        if len(gradebook.students) == 0:
            print("No students found.")
        else:
            for student in gradebook.students.values():
                student.display_info()
                print("--------------------------")

    # Add Course
    elif choice == "3":

        course_code = input("Course Code: ")
        course_name = input("Course Name: ")

        course = Course(course_code, course_name)
        gradebook.add_course(course)

    # Enroll Student
    elif choice == "4":

        student_id = input("Student ID: ")
        course_code = input("Course Code: ")

        gradebook.enroll_student(student_id, course_code)

    # Add Assessment
    elif choice == "5":

        course_code = input("Course Code: ")

        print("1. Quiz")
        print("2. Exam")
        print("3. Project")

        assessment_type = input("Choose type: ")

        title = input("Assessment Title: ")
        max_score = int(input("Max Score: "))

        if assessment_type == "1":
            assessment = Quiz(title, max_score)

        elif assessment_type == "2":
            assessment = Exam(title, max_score)

        elif assessment_type == "3":
            assessment = Project(title, max_score)

        else:
            print("Invalid choice.")
            continue

        gradebook.add_assessment(course_code, assessment)

    # Record Grade
    elif choice == "6":

        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        title = input("Assessment Title: ")
        score = float(input("Score: "))

        gradebook.record_grade(student_id, course_code, title, score)

    # Student Report
    elif choice == "7":

        student_id = input("Student ID: ")
        gradebook.show_report(student_id)

    # Search Student
    elif choice == "8":

        keyword = input("Enter Student ID or Name: ")

        student = gradebook.search_student(keyword)

        if student:
            student.display_info()
        else:
            print("Student not found.")

    # Update Student Email
    elif choice == "9":

        student_id = input("Student ID: ")
        new_email = input("New Email: ")

        gradebook.update_student(student_id, new_email)

    # Delete Student
    elif choice == "10":

        student_id = input("Student ID: ")

        gradebook.delete_student(student_id)

    # Dashboard
    elif choice == "11":

        print("\n===== Dashboard =====")
        print("Total Students:", len(gradebook.students))
        print("Total Courses:", len(gradebook.courses))

        total_assessments = 0

        for course in gradebook.courses.values():
            total_assessments += len(course.assessments)

        print("Total Assessments:", total_assessments)

    # Top Student
    elif choice == "12":

        gradebook.top_student()

    # Course Statistics
    elif choice == "13":

        gradebook.course_statistics()

    # Exit
    elif choice == "0":

        print("Goodbye!")
        break

    else:
        print("Invalid choice.")