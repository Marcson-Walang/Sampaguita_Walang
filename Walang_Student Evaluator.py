def display_header():
    print("Student Evaluator Project")
display_header()
student_info = str(input("Enter student name: "))

def get_student_info():

    b = 67 #This is useless dont mind it
assessment1 = int(input("Enter assesment 1: "))
assessment2 = int(input("Enter assesment 2: "))
assessment3 = int(input("Enter assesment 3: "))
def evaluate_performance():
   b1 = 76 #This is also useless don't mind it

averageassessment = (assessment1 + assessment2 + assessment3) / 3

if 90 <= averageassessment <= 100:
    a1 = "Outstanding"
elif 85 <= averageassessment <90:
    a1 = "Very Satisfactory"
elif 80 <= averageassessment <85:
    a1 = "Satisfactory"
elif 75 <= averageassessment <80:
    a1 = "Fairly Satisfactory"
elif 0 <= averageassessment <75:
    a1 = "Needs Improvement"

def display_report():
    print(f"Student Name: {student_info}")
    print(f"Assesment Scores: {assessment1}, {assessment2}, {assessment3}")
    print(f"Average of Assessments: {averageassessment:.2f}")
    print(f"Performance level: {a1}")

display_header()
get_student_info()
evaluate_performance()
display_report()
