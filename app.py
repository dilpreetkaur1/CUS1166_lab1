from mymodules.model import Student
from mymodules.math_utils import average_grade

if __name__ == '__main__':
    roster = [Student("Cindy", 85),
              Student("Barbara", 55),
              Student("Alex", 90),
              Student("Fred", 95),
              Student("Chelsea", 75),
              Student("Brianna", 66),
              Student("Chiara", 89),
              Student("Kevin", 95),
              Student("Xiao", 80),
              Student("Sophia", 97)]

    for i in roster:
        i.print_student_info()

    print("Average grade: " + str(average_grade(roster)))
