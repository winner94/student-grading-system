#Student Grading System

# -- DATA -- 
# list of students with points
students = {
    "Anna" : 43,
    "Andrzej" : 54,
    "Bożena" : 65,
    "Bożydar" : 75,
    "Czesław" : 92
}

# -- FUNCTIONS --
'''
Points to grades:
0-49 -> 2
50-64 -> 3
65-79 -> 4
80-100 -> 5
'''
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
grades = dict()
passed = []

#   dictionary: student --> grade
for k, v in students.items():
    grades[k] = get_grade(v)
    if has_passed(grades[k]):
        print(f"{k} {v} - Passed")
        passed.append(k)
    else:
        print(f"{k} {v} - Failed")

# print group average
grades_length = len(grades)
grades_sum = sum(grades.values())
grades_average = grades_sum / grades_length
print(f"Group Average {grades_average}")

# print who pass
print(f"Passed: {passed}")