import sys

GRADE_BOUNDARY_A_STAR = 90
OUT_OF_BOUNDS_UPPER = 101
GRADE_A_STAR = "A*"

def convert_to_grade(mark):
    if mark <= -1 or mark >= OUT_OF_BOUNDS_UPPER:
        return "Unknown - Invalid mark"

    if mark >= GRADE_BOUNDARY_A_STAR:
        return GRADE_A_STAR
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


def grade_is_higher_than_target(grade, target_grade):
    # If your target was A* then you can't beat it
    if target_grade == GRADE_A_STAR:
        return False

    # A* beats all other grades
    if grade == GRADE_A_STAR:
        return True
    # Alphabetically A is less than B, but for grades it is better
    elif grade < target_grade:
        return True
    else:
        return False


def target_grade_is_valid(target_grade):
    if target_grade in [GRADE_A_STAR, "A", "B", "C", "D", "F"]:
        return True

    return False


def process_student_mark_and_grade():
    # Get mark and convert to grade
    mark = input("Enter the mark: ")

    if mark.isdigit():
        mark = int(mark)
        grade = convert_to_grade(mark)
        print(f"The grade was {grade}")
    else:
        print("Invalid mark - not numeric")
        sys.exit() # can't continue with rest of program

    # Get target grade
    target_grade = input("What was the target grade? ")

    if target_grade_is_valid(target_grade):
        # Compare actual grade to target and display appropriate message
        if grade_is_higher_than_target(grade, target_grade):
            print("The student beat their target. Congratulate them!")
        elif grade == target_grade:
            print("The student achieved their target. Congratulate them!")
        else:
            print("The student did not achieve their target this time. Encourage them!")
    else:
        print("Invalid target grade")


finished = False

while not finished:

    process_student_mark_and_grade()

    response = input("Have you finished? ")
    if response == "y" or response == "Y":
        finished = True




"""
Test Data

For convert to grade.
100 -> A*
90 -> A*
89 -> A
80 -> A
79 -> B
70 -> B
69 -> C
60 -> C
59 -> D
50 -> D
49 -> F

-1 -> Unknown - Invalid mark
101 -> Unknown - Invalid mark
hello -> Invalid mark - not numeric


For actual grade to target grade comparison.
A* / A -> You beat your target, very well done.
A / B -> You beat your target, very well done.
B / C -> You beat your target, very well done.
C / D -> You beat your target, very well done.
D / F -> You beat your target, very well done.
? / A* -> ??????????????

A* / A* -> You achieved your target, well done.
A / A -> You achieved your target, well done.
B / B -> You achieved your target, well done.
C / C -> You achieved your target, well done.
D / D -> You achieved your target, well done.
F / F -> You achieved your target, well done.

A / A* -> You did not achieve your target this time. Keep working!
B / A -> You did not achieve your target this time. Keep working!
C / B -> You did not achieve your target this time. Keep working!
D / C -> You did not achieve your target this time. Keep working!
F / D -> You did not achieve your target this time. Keep working!

A / E -> Invalid target grade
A / hello -> Invalid target grade

"""
