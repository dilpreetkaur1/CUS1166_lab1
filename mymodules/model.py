class Student:

    def __init__(self, student_name, student_grade):
        self.student_name = student_name
        self.student_grade = student_grade

    def set_grade(self, student_grade):
        self.student_grade = student_grade

    def get_grade(self):
        return self.student_grade

    def print_student_info(self):
        print(str(self.student_grade))
