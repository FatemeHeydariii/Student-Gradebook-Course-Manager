from assessment import Quiz, Exam, Project

q1 = Quiz("Quiz 1", 10)
q2 = Exam("Midterm", 100)
q3 = Project("Final project", 100)

q1.display_info()
print(q1.calculate_percentage(8))
print(q1.grade_message(8))

print()

e1.display_info()
print(e1.grade_message(75))

print()

p1.display_info()
print(p1.grade_message(95))