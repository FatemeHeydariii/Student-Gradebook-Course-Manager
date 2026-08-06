class Assessment:

    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        return (score / self.max_score) * 100

    def display_info(self):
        print(self.title, "- Max Score: ", self.max_score)

    def grade(self, score):
        if self.calculate_percentage(score) >= 55:
            return "Passed"
        else:
            return "Failed"


class Quiz(Assessment):

    def display_info(self):
        print("Quiz: ", self.title, "- Max Score: ", self.max_score)

    def grade_message(self, score):
        if self.calculate_percentage(score) >= 80:
            return "Great Quiz result!"
        else:
            return "Need more practice"


class Exam(Assessment):

    def display_info(self):
        print("Exam: ", self.title, "Max Score: ", self.max_score)

    def grade_message(self, score):
        if self.calculate_percentage(score) >= 55:
            return "Passed Exam"
        else:
            return "Failed Exam"


class Project(Assessment):

    def display_info(self):
        print("Project: ", self.title, "- Max Score: ", self.max_score)

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 90:
            return "Excellent Project"
        elif percentage >= 55:
            return "Project submitted"
        else:
            return " Project needs improvement"