#Student Grading System

# -- DATA -- 
# list of students with grades
# Grades between 
students = {
    "Anna" : 43,
    "Andrzej" : 54,
    "Bożena" : 65,
    "Bożydar" : 75,
    "Czesław" : 92
}

grades = dict()
'''
Points to grades:
0-49 -> 2
50-64 -> 3
65-79 -> 4
80-100 -> 5
'''

# -- FUNCTIONS --
# function: get grade
def get_grade(points):
    if points < 50:
        return 2
    elif points < 65:
        return 3
    elif points < 80:
        return 4
    elif points <= 100:
        return 5
    else:
        print(f"Error: points out of range")
        return 0
# function: check if student passed
def has_passed(grade):
    return grade > 2

# --- MAIN LOGIC ---
#   get_grade tests
#   print(get_grade(43))        # expected 2
#   print(get_grade(54))        # expected 3
#   print(get_grade(92))        # expected 5
# dictionary: student --> grade
for k, v in students.items():
    grades[k] = get_grade(v)

# print results
for k, v in grades.items():
    if has_passed(v):
        print(f"{k} {v} - Passed")
    else:
        print(f"{k} {v} - Failed")
# print who pass
# print group average

for k, v in students.items():
    grades[k] = get_grade(v)

#print(grades)